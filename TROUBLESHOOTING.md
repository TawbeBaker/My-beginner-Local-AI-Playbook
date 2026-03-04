# Troubleshooting Guide

Common issues and their solutions for local AI development.

---

## 🔧 Quick Diagnostics

### Problem Checklist

Before troubleshooting, verify:
- [ ] Latest version of tool installed
- [ ] Sufficient disk space (50GB+ free)
- [ ] Sufficient RAM (8GB+ available)
- [ ] GPU drivers updated (if using GPU)
- [ ] Internet connection working (for downloads)
- [ ] Antivirus not blocking (temporarily disable to test)

---

## 🦙 Ollama Issues

### Ollama: "Connection refused" or "Cannot connect"

**Symptoms:** Cannot connect to Ollama API

**Solutions:**

```bash
# 1. Check if Ollama is running
# Windows
tasklist | findstr ollama

# Mac/Linux
ps aux | grep ollama

# 2. Start Ollama manually
ollama serve

# 3. Check port (should see 11434)
netstat -ano | findstr :11434

# 4. Try connecting
curl http://localhost:11434/api/tags

# 5. If still failing, restart Ollama
# Windows: Kill process and restart
# Mac/Linux: pkill ollama && ollama serve
```

**Still not working?**
- Check firewall settings
- Reinstall Ollama
- Check logs: `~/.ollama/logs/` (Mac/Linux) or `%LOCALAPPDATA%\Ollama\logs\` (Windows)

---

### Ollama: "Model not found"

**Symptoms:** Error when trying to use a model

**Solutions:**

```bash
# 1. List installed models
ollama list

# 2. Pull the model you need
ollama pull llama3.2

# 3. Verify it appears in list
ollama list

# 4. Try running it
ollama run llama3.2

# 5. If specific version needed
ollama pull llama3.2:3b
```

**Common model names:**
- `llama3.2` or `llama3.2:8b` (8 billion parameters)
- `llama3.2:3b` (3 billion, smaller/faster)
- `mistral`, `codellama`, `deepseek-coder`

---

### Ollama: Very slow on CPU

**Symptoms:** Taking minutes per response

**Solutions:**

```bash
# 1. Use smaller models
ollama pull llama3.2:3b    # Instead of 8b

# 2. Use more CPU threads
# Set in environment
export OLLAMA_NUM_THREADS=8

# 3. Use quantized models (Ollama does this automatically)

# 4. Reduce context length
# In code, limit message history to 3-5 messages

# 5. Close other applications
```

**Expected speeds (CPU):**
- Small model (3B): 5-15 tokens/sec
- Medium model (7B): 2-8 tokens/sec
- Large model (13B+): 0.5-3 tokens/sec

---

### Ollama: Out of memory

**Symptoms:** Crash or "out of memory" error

**Solutions:**

```bash
# 1. Use smaller model
ollama pull llama3.2:3b

# 2. Close other applications

# 3. Restart Ollama
ollama serve

# 4. Check available RAM
# Windows: Task Manager > Performance
# Mac: Activity Monitor
# Linux: free -h

# 5. Increase swap/pagefile (if needed)
# Windows: System Properties > Advanced > Performance > Virtual Memory
# Linux: sudo swapon --show
```

---

## 🐋 Docker & n8n Issues

### Docker: Cannot start containers

**Symptoms:** `docker-compose up` fails

**Solutions:**

```bash
# 1. Check Docker is running
docker --version
docker ps

# 2. Restart Docker Desktop
# Windows/Mac: Quit and reopen Docker Desktop

# 3. Check for port conflicts
netstat -ano | findstr :5678    # n8n port
netstat -ano | findstr :6333    # Qdrant port
netstat -ano | findstr :5432    # PostgreSQL port

# 4. Stop conflicting services or change ports

# 5. Remove old containers and restart
docker-compose down
docker-compose up -d

# 6. Check logs
docker-compose logs
```

---

### Docker: "No space left on device"

**Symptoms:** Disk full error

**Solutions:**

```bash
# 1. Check Docker disk usage
docker system df

# 2. Remove unused images/containers
docker system prune -a

# 3. Remove specific containers
docker ps -a                    # List all
docker rm <container_id>        # Remove specific

# 4. Free host disk space
# Delete unnecessary files, move data

# 5. Increase Docker disk allocation
# Docker Desktop > Settings > Resources > Disk limit
```

---

### n8n: Cannot access dashboard

**Symptoms:** `http://localhost:5678` not loading

**Solutions:**

```bash
# 1. Verify container is running
docker ps | grep n8n

# 2. Check logs
docker logs n8n

# 3. Verify port mapping
docker ps -a    # Look for 0.0.0.0:5678->5678/tcp

# 4. Try different browser or incognito

# 5. Check firewall

# 6. Restart n8n container
docker restart n8n

# 7. If still failing, remove and recreate
docker-compose down
docker-compose up -d
```

---

## 🎨 Stable Diffusion Issues

### SD: Black images generated

**Symptoms:** All generated images are black

**Solutions:**

**Method 1: Add VAE flag**
```
1. Open Stable Diffusion WebUI settings
2. Command line arguments
3. Add: --no-half-vae
4. Restart WebUI
```

**Method 2: Update GPU drivers**
```
1. Visit nvidia.com/drivers
2. Download latest drivers
3. Install and restart
```

**Method 3: Try different sampler**
```
1. In WebUI, change Sampler to:
   - Euler a
   - DPM++ 2M Karras
2. Generate again
```

**Method 4: Use different checkpoint**
```
1. Try a different model
2. Download from CivitAI
3. Place in models/Stable-diffusion/
4. Reload and test
```

---

### SD: "CUDA out of memory"

**Symptoms:** Error during image generation

**Solutions:**

**Quick fixes:**
```
1. Generate smaller images (512x512)
2. Reduce batch size to 1
3. Lower CFG scale (to 7-8)
4. Reduce sampling steps (to 20-30)
```

**Launch arguments (add to settings):**
```
--lowvram        # For <4GB VRAM
--medvram        # For 4-8GB VRAM
--xformers       # Memory optimization
--opt-split-attention-v1
```

**Memory management:**
```
1. Close browser tabs
2. Close other GPU applications
3. Restart WebUI
4. Restart computer (clears VRAM)
```

---

### SD: Very slow generation

**Symptoms:** 5+ minutes per image

**Solutions:**

```
1. Verify GPU is being used:
   - Open nvidia-smi (Windows CMD)
   - Should show python.exe using GPU

2. Enable xFormers:
   - WebUI settings
   - Add --xformers to launch args
   - Restart

3. Reduce quality settings:
   - Steps: 20 instead of 50
   - Size: 512x512 instead of 1024x1024

4. Update GPU drivers

5. Check GPU isn't throttling:
   - Clean dust from computer
   - Check temperatures (nvidia-smi)
```

**Expected speeds (RTX 3060):**
- 512x512, 20 steps: ~10 seconds
- 768x768, 30 steps: ~25 seconds
- 1024x1024, 50 steps: ~60+ seconds

---

### SD: Extensions not working

**Symptoms:** Extensions fail to install or load

**Solutions:**

```bash
# 1. Update WebUI
cd stable-diffusion-webui
git pull

# 2. Update extensions
# WebUI > Extensions > Check for updates

# 3. Manually reinstall extension
cd extensions
rm -rf <extension-name>
git clone <extension-repo-url>

# 4. Check Python dependencies
pip install -r requirements.txt

# 5. Check extension compatibility
# Some extensions need specific WebUI versions
```

---

## 🎤 Whisper Issues

### Whisper: "No module named 'openai'"

**Symptoms:** Import error when running Whisper

**Solutions:**

```bash
# Install Whisper
pip install -U openai-whisper

# If still failing, use full path
python -m pip install openai-whisper

# Verify installation
python -c "import whisper; print(whisper.__version__)"

# If multiple Python versions
python3 -m pip install openai-whisper
```

---

### Whisper: "ffmpeg not found"

**Symptoms:** Cannot process audio files

**Solutions:**

**Windows:**
```powershell
# Using Chocolatey
choco install ffmpeg

# Or download manually:
# 1. Visit ffmpeg.org
# 2. Download Windows build
# 3. Add to PATH
```

**Mac:**
```bash
brew install ffmpeg
```

**Linux:**
```bash
sudo apt install ffmpeg
```

**Verify:**
```bash
ffmpeg -version
```

---

### Whisper: Transcription is gibberish

**Symptoms:** Wrong language or nonsense output

**Solutions:**

```bash
# 1. Specify language explicitly
whisper audio.mp3 --language English

# 2. Try larger model
whisper audio.mp3 --model medium    # Instead of base/tiny

# 3. Check audio quality
# - Whisper works best with clear speech
# - Reduce background noise
# - Try different audio file to test

# 4. Update Whisper
pip install -U openai-whisper

# 5. Try different task
whisper audio.mp3 --task transcribe  # Instead of translate
```

---

## 🔨 Training & Fine-tuning Issues

### Training: "CUDA out of memory"

**Symptoms:** Crash during training

**Solutions:**

```python
# 1. Reduce batch size
batch_size = 1  # Instead of 4 or 8

# 2. Use gradient accumulation
gradient_accumulation_steps = 4

# 3. Use LoRA instead of full fine-tune
# Requires 10x less VRAM

# 4. Enable gradient checkpointing
gradient_checkpointing = True

# 5. Use 8-bit optimizer
use_8bit_adam = True

# 6. Reduce model size
# Train 7B instead of 13B
```

**For Kohya:**
```
- Lower resolution (512 instead of 768)
- Disable cached latents caching
- Use --lowvram flag
```

---

### Training: Loss not decreasing

**Symptoms:** Training doesn't improve model

**Solutions:**

```python
# 1. Increase learning rate
learning_rate = 2e-5  # Instead of 1e-6

# 2. Check data format
# Verify examples are correct format

# 3. Train longer
num_train_epochs = 5  # Instead of 1

# 4. Reduce batch size (helps with stability)
per_device_train_batch_size = 2

# 5. Check for data loading errors
# Print first few batches to verify
```

**Data quality checklist:**
- [ ] All examples in correct format?
- [ ] Labels correct and consistent?
- [ ] Sufficient variety in data?
- [ ] No corrupted files?

---

### Training: Model outputs gibberish after fine-tune

**Symptoms:** Trained model worse than original

**Causes & Solutions:**

**Overfitting:**
```python
# Reduce epochs
num_train_epochs = 1  # Instead of 10

# Lower learning rate
learning_rate = 1e-5  # Instead of 1e-4

# Add validation set to monitor
```

**Catastrophic forgetting:**
```python
# Use lower LoRA rank
lora_r = 8  # Instead of 64

# Lower learning rate
learning_rate = 1e-5

# Mix in general examples (not just specialized)
```

**Bad data:**
```
# Review training data
# Fix inconsistencies
# Remove low-quality examples
```

---

## 🌐 Network & API Issues

### Cannot download models from Hugging Face

**Symptoms:** Timeout or very slow downloads

**Solutions:**

```bash
# 1. Use huggingface-cli with resume
pip install huggingface-hub
huggingface-cli download <model-id> --resume-download

# 2. Use aria2c (faster multi-threaded downloader)
aria2c -x 16 -s 16 <model-url>

# 3. Download via browser
# Visit Hugging Face, click Files, download manually

# 4. Use mirror (if available)
# Check for regional mirrors in your country

# 5. Increase timeout
export HF_HUB_DOWNLOAD_TIMEOUT=300
```

---

### API rate limits

**Symptoms:** "Rate limit exceeded" errors

**Solutions:**

**For Hugging Face:**
```bash
# Get API token
# huggingface.co > Settings > Access Tokens

# Login
huggingface-cli login

# Token gives higher rate limits
```

**For GitHub (downloading repos):**
```bash
# Use SSH instead of HTTPS
git clone git@github.com:user/repo.git

# Or get GitHub token
# github.com > Settings > Developer settings > Tokens
```

---

## 💻 General System Issues

### High RAM usage

**Symptoms:** System becomes slow

**Solutions:**

```
1. Close browser (especially Chrome)
2. Only run one AI tool at a time
3. Use smaller models
4. Increase page file/swap
5. Upgrade RAM (if budget allows)

For Windows:
- Ctrl+Shift+Esc > Performance tab
- Check memory usage
- Close heavy applications

For Mac:
- Activity Monitor
- Sort by Memory
- Quit memory-heavy apps
```

---

### High CPU temperature

**Symptoms:** Computer very hot, throttling

**Solutions:**

```
1. Clean dust from computer
   - Compressed air
   - Focus on fans and vents

2. Improve airflow
   - Elevate laptop
   - Remove obstructions
   - Use cooling pad

3. Reduce workload
   - Use GPU instead of CPU
   - Use smaller models
   - Take breaks between generations

4. Check thermal paste (advanced)
   - If computer is old (3+ years)
   - May need reapplication

5. Monitor temperatures
   - Windows: HWMonitor
   - Mac: iStat Menus
   - Linux: sensors command
```

**Safe temperatures:**
- CPU: <80°C normal, <90°C max
- GPU: <85°C normal, <90°C max

---

### Disk space filling up quickly

**Symptoms:** Running out of storage

**Solutions:**

```bash
# 1. Find large directories
# Windows: Use WinDirStat
# Mac: Use DaisyDisk or ncdu
# Linux: du -sh * | sort -h

# 2. Clean Ollama models
ollama list             # See installed models
ollama rm <model>       # Remove unused

# 3. Clean Docker
docker system df        # Check usage
docker system prune -a  # Remove unused

# 4. Clean Stable Diffusion
# models/ folder can be huge
# Remove unused checkpoints

# 5. Clear pip cache
pip cache purge

# 6. Clear browser cache
```

**Storage estimates:**
- Ollama model (7B): 4-8GB each
- SD checkpoint: 2-7GB each
- Docker images: 1-5GB each
- Training outputs: 100MB-10GB

---

## 🆘 Getting More Help

### Still stuck?

**1. Check logs:**
```bash
# Ollama logs
~/.ollama/logs/           # Mac/Linux
%LOCALAPPDATA%\Ollama\logs\  # Windows

# Docker logs
docker logs <container-name>

# System logs
# Windows: Event Viewer
# Mac: Console.app
# Linux: /var/log/
```

**2. Search for error message:**
```
1. Copy exact error message
2. Google: "<error message> <tool name>"
3. Check GitHub Issues of tool
4. Search Reddit r/LocalLLaMA
```

**3. Ask community:**

**Where to ask:**
- r/LocalLLaMA (general AI)
- r/StableDiffusion (image gen)
- Tool-specific Discord
- GitHub Discussions (this repo)

**What to include:**
```
1. What you're trying to do
2. Exact error message
3. System specs (OS, RAM, GPU)
4. What you've already tried
5. Relevant logs
```

**4. Create GitHub Issue:**

If you think it's a bug in the guide or examples:
```
1. Go to GitHub repository
2. Issues > New Issue
3. Provide details (use template)
4. Be patient for response
```

---

## 📋 System Information Gathering

**When asking for help, gather this info:**

**Windows:**
```powershell
# System info
systeminfo | findstr /B /C:"OS Name" /C:"Total Physical Memory"

# GPU info
nvidia-smi

# Python version
python --version

# Installed packages
pip list
```

**Mac:**
```bash
# System info
system_profiler SPSoftwareDataType SPHardwareDataType

# GPU info (for Apple Silicon)
system_profiler SPDisplaysDataType

# Python version
python3 --version

# Installed packages
pip3 list
```

**Linux:**
```bash
# System info
cat /etc/os-release
free -h
lscpu

# GPU info
nvidia-smi  # NVIDIA
lspci | grep VGA  # Other

# Python version
python3 --version

# Installed packages
pip3 list
```

---

## ✅ Preventive Measures

**Avoid future issues:**

```
1. Keep tools updated
   - Check for updates weekly
   - Read release notes

2. Monitor resources
   - Check disk space regularly
   - Monitor GPU/CPU temps

3. Backup important data
   - Fine-tuned models
   - Training datasets
   - Configuration files

4. Document your setup
   - Note what works
   - Save working configs
   - Track model versions

5. Test incrementally
   - Don't change everything at once
   - Test after each change
   - Keep last working state
```

---

**Didn't find your issue? Open a GitHub Discussion or Issue!**

*Last Updated: March 2026*
