import os
import re
import json
from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel

load_dotenv()

# --- CONFIGURAÇÃO OPENROUTER ---
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY,
)

class JobOptimizationRequest(BaseModel):
    resume_text: str
    job_description: str

class PDFRequest(BaseModel):
    curriculo_otimizado: str

# Função de Apoio
def optimize_with_openrouter(resume, job):
    try:
        response = client.chat.completions.create(
            extra_headers={
                "HTTP-Referer": "http://localhost:8000",
                "X-Title": "Resume Optimizer", 
            },
            model="meta-llama/llama-3.3-70b-instruct",
            messages=[
                {
                    "role": "system",
                    "content": """Você é um Especialista em Recrutamento e Seleção de TI com foco em ATS (Applicant Tracking Systems). 
                    Sua tarefa é reescrever o currículo do usuário para que ele tenha o máximo de compatibilidade com a descrição da vaga fornecida.

                    DIRETRIZES DE OTIMIZAÇÃO:
                    1. ANÁLISE DE PALAVRAS-CHAVE: Identifique as tecnologias, metodologias (Agile, Scrum) e soft skills mais importantes na descrição da vaga e integre-as naturalmente no currículo.
                    2. FOCO EM RESULTADOS: Nas experiências profissionais, não apenas liste tarefas. Use verbos de ação e tente quantificar conquistas (ex: "Aumentou a eficiência em X%", "Reduziu o tempo de resposta em Y").
                    3. ADAPTAÇÃO DE SOBRE/RESUMO: Reescreva o resumo profissional para destacar exatamente os anos de experiência e as tecnologias que a vaga pede logo de início.
                    4. MAPEAMENTO DE HABILIDADES: Se o usuário tem uma habilidade que a vaga pede, mas ela está "escondida" ou mal descrita, dê destaque a ela para mostrar valor imediato à empresa.
                    5. TOM DE VOZ: Mantenha um tom profissional, direto e confiante.

                    REGRAS DE FORMATO:
                    - Mantenha o currículo completo, não resuma apenas as partes alteradas.
                    - Use Markdown para estruturar o texto (# para Nome, ## para Seções, ### para Cargos/Empresas).
                    - Use listas (hifens) para as responsabilidades.
                    
                    SAÍDA OBRIGATÓRIA:
                    Sua saída deve ser EXCLUSIVAMENTE um objeto JSON válido, sem texto antes ou depois, seguindo esta estrutura:
                    {
                        "curriculo_otimizado": "texto em markdown aqui",
                        "match_score_original": número de 0 a 100,
                        "match_score_otimizado": número de 0 a 100,
                        "sugestao_cursos": ["curso 1", "curso 2"],
                        "analise_gap": "breve explicação do que faltava no currículo original e o que foi melhorado"
                    }"""
                },
                {
                    "role": "user",
                    "content": f"Aja como o recrutador. Otimize este currículo para esta vaga específica.\n\nCURRÍCULO ORIGINAL:\n{resume}\n\nDESCRIÇÃO DA VAGA:\n{job}"
                }
            ],
            max_tokens=3000,
            temperature=0.3
        )
        
        content = response.choices[0].message.content
        match = re.search(r'\{.*\}', content, re.DOTALL)
        return json.loads(match.group(), strict=False) if match else {"error": "JSON não encontrado"}
    except Exception as e:
        raise e