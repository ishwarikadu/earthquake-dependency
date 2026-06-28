from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import routers
from backend.routes import earthquake_r, dependency_r, risk_r

app = FastAPI(
    title="Dependency Earthquake API",
    description="AI-powered cascading failure simulation platform",
    version="1.0.0"
)

# CORS configuration (important for frontend connection later)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # later replace with frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root route
@app.get("/")
def root():
    return {
        "message": "Dependency Earthquake Backend Running"
    }

# Health check route
@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }

# Include routers
app.include_router(earthquake_r.router)
app.include_router(dependency_r.router)
app.include_router(risk_r.router)