from fpdf import FPDF
import re

class ResumePDF(FPDF):
    def header(self):
        pass

    def add_markdown_content(self, markdown_text):
        # Definir margens globais na página
        margin_left = 20
        margin_right = 20
        self.set_left_margin(margin_left)
        self.set_right_margin(margin_right)      

        # Largura útil real: 210mm (A4) - margens
        w_util = 210 - margin_left - margin_right 

        clean_text = markdown_text.replace('—', '-').replace('–', '-').replace('•', '-')
        clean_text = clean_text.replace('“', '"').replace('”', '"').replace('‘', "'").replace('’', "'")
        
        # Remove links markdown [texto](link) mantendo apenas o texto
        clean_text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', clean_text)

        for line in clean_text.split('\n'):
            line = line.strip()
            
            # Converte para Latin-1 linha por linha
            line = line.encode('latin-1', 'replace').decode('latin-1')
            
            if not line:
                self.ln(3)
                continue

            # --- TÍTULO PRINCIPAL (#) ---
            if line.startswith("# "):
                self.set_text_color(0, 0, 0) # Preto
                self.set_font("Helvetica", "B", 16)
                txt = line.replace("# ", "").lstrip('? ')
                self.multi_cell(w_util, 10, txt, new_x="LMARGIN", new_y="NEXT")
            
            # --- SUBTÍTULOS (##) - APENAS ESTES FICAM AZUIS ---
            elif line.startswith("## "):
                self.ln(2)
                self.set_text_color(20, 50, 100) # Azul Marinho Profissional
                self.set_font("Helvetica", "B", 13)
                txt = line.replace("## ", "").lstrip('? ')
                self.multi_cell(w_util, 8, txt, new_x="LMARGIN", new_y="NEXT")
                self.set_text_color(0, 0, 0) # RESET PARA PRETO IMEDIATAMENTE
            
            # --- EXPERIÊNCIAS / CARGOS (###) ---
            elif line.startswith("### "):
                self.set_text_color(0, 0, 0) # Garante preto
                self.set_font("Helvetica", "B", 11)
                txt = line.replace("### ", "").lstrip('? ')
                self.multi_cell(w_util, 6, txt, new_x="LMARGIN", new_y="NEXT")
            
            # --- TEXTO COMUM E LISTAS ---
            else:
                self.set_text_color(0, 0, 0) # Garante preto
                self.set_font("Helvetica", size=10)
                # Remove negritos do markdown e trata o marcador de lista
                clean_line = line.replace("**", "").replace("*", "-")
                
                # Se a linha começar com uma interrogação residual, troca por hífen
                if clean_line.startswith("?"): 
                    clean_line = "-" + clean_line[1:]
                
                self.multi_cell(w_util, 5, clean_line, new_x="LMARGIN", new_y="NEXT")