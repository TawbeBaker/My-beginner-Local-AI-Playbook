# ⚡ Quick Start Guide - Get Running in 30 Minutes

This is the **fastest path** to getting your local AI environment running. Follow these steps in order.

---

## Step 1: Install Docker (10 minutes)

**Windows:**
```
1. Download Docker Desktop: https://www.docker.com/products/docker-desktop
2. Run installer
3. Restart computer
4. Open Docker Desktop (wait for it to start)
5. Verify: Open PowerShell and run: docker --version
```

**Mac:**
```
1. Download Docker Desktop for Mac
2. Drag to Applications folder
3. Launch Docker
4. Verify: Open Terminal and run: docker --version
```

**Linux:**
```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo systemctl start docker
sudo usermod -aG docker $USER
# Log out and back in
docker --version
```

---

## Step 2: Install Ollama (5 minutes)

**All Platforms:**
```
1. Visit: https://ollama.com
2. Download for your OS
3. Install
4. Verify: ollama --version
```

**Pull your first model:**
```bash
# Start with a small, fast model
ollama pull llama3.2:3b

# Test it
ollama run llama3.2:3b
# Type: "Hello! Introduce yourself."
# Press Ctrl+D to exit
```

**Common models to try:**
```bash
ollama pull mistral           # 7B - excellent quality
ollama pull codellama         # for programming tasks
ollama pull deepseek-coder    # best for code
ollama pull llama3.2          # Meta's latest
```

---

## Step 3: Set Up n8n (10 minutes)

**Clone and start:**
```bash
# Open terminal/PowerShell
git clone https://github.com/n8n-io/self-hosted-ai-starter-kit.git
cd self-hosted-ai-starter-kit

# Start all services
docker-compose up -d

# Wait 1-2 minutes for services to start
# Check status: docker ps
```

**Access your tools:**
```
n8n:          http://localhost:5678
Qdrant UI:    http://localhost:6333/dashboard
PostgreSQL:   localhost:5432 (user: postgres, password: in .env file)
```

**First n8n workflow:**
```
1. Open http://localhost:5678
2. Create account (local only)
3. Click "New Workflow"
4. Add node → AI → Ollama
5. Add node → Chat → Chat Trigger
6. Connect them
7. Configure Ollama node to use your model
8. Click "Test Workflow"
9. Chat with your AI!
```

---

## Step 4: First Image Generation (10 minutes)

**Install Stability Matrix:**
```
1. Download: https://github.com/LykosAI/StabilityMatrix/releases
2. Run installer
3. Choose installation folder (needs 20GB+)
4. Click "Add Package"
5. Select "Stable Diffusion WebUI"
6. Click Install (wait 5-10 min)
7. Click Launch
```

**Generate first image:**
```
1. Wait for WebUI to load
2. In prompt box: "A serene mountain landscape at sunset, detailed oil painting"
3. Click "Generate"
4. Wait ~30 seconds
5. Enjoy your first AI-generated image!
```

---

## Step 5: Install Whisper (5 minutes)

**If you have Python:**
```bash
pip install -U openai-whisper
# Install ffmpeg (needed for audio processing)
# Windows: choco install ffmpeg
# Mac: brew install ffmpeg
# Linux: apt install ffmpeg

# Test
whisper test_audio.mp3 --model small
```

**If you don't have Python:**
```
Download Whisper Desktop:
- Windows: https://github.com/Const-me/Whisper/releases
- Mac: MacWhisper from App Store
```

---

## ✅ You're Done!

**What you now have:**
- ✅ Local language models (Ollama)
- ✅ AI workflow automation (n8n)
- ✅ Vector database (Qdrant)
- ✅ Image generation (Stable Diffusion)
- ✅ Speech-to-text (Whisper)

---

## What's Next?

**Beginner Projects:**
1. **Personal AI Assistant**: Use n8n to create a chatbot that answers questions
2. **Image Generator**: Make custom images with Stable Diffusion
3. **Transcriber**: Convert voice notes to text with Whisper

**Learn More:**
- Read the full guide: [README.md](README.md)
- Explore n8n workflows: https://n8n.io/workflows
- Try different Ollama models: https://ollama.com/library

---

## Troubleshooting

**Ollama not found:**
```bash
# Make sure it's running
ollama serve

# In another terminal
ollama ps  # shows running models
```

**Docker issues:**
```bash
# Restart Docker Desktop
# Or in terminal:
docker-compose down
docker-compose up -d
```

**Stable Diffusion slow/crashes:**
```
- Use smaller image sizes (512x512)
- Close other applications
- Check GPU drivers are updated
- Try --lowvram flag in settings
```

**Out of disk space:**
```
Ollama models: ~/.ollama/models (del old models)
Stable Diffusion: Check Stability Matrix folder
Docker: docker system prune -a (frees space)
```

---

## Resource Usage

**Expect to use:**
- Disk: 50-100GB (models and tools)
- RAM: 8-16GB actively running
- GPU: Optional but highly recommended for image gen

**If limited resources:**
- Use smaller models (3B instead of 7B)
- Generate smaller images
- Run one tool at a time
- Use CPU-based models

---

**Need Help?**  
- Check main guide: [README.md](README.md)
- Community: r/LocalLLaMA, r/StableDiffusion
- Issues: Open an issue in this repo

**Happy AI Building! 🚀**
