from fastapi import FastAPI, HTTPException, Response
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from .dependencies import JobOptimizationRequest, PDFRequest, optimize_with_openrouter
from utils.pdf_generator import ResumePDF

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/optimize")
async def optimize_resume(data: JobOptimizationRequest):
    try:
        resultado = optimize_with_openrouter(data.resume_text, data.job_description)
        return {"status": "sucesso", "data": resultado}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/download-pdf")
async def download_pdf(data: PDFRequest):
    try:
        pdf = ResumePDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        
        pdf.add_markdown_content(data.curriculo_otimizado)
        
        pdf_bytes = bytes(pdf.output()) 
        
        return Response(
            content=pdf_bytes,
            media_type="application/pdf",
            headers={"Content-Disposition": "attachment; filename=curriculo.pdf"}
        )
    except Exception as e:
        print(f"Erro no PDF: {e}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)