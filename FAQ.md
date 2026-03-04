# Frequently Asked Questions (FAQ)

Common questions and answers about local AI development.

---

## General Questions

### What is "local AI"?

Local AI means running AI models on your own computer instead of using cloud services like OpenAI's API. You have complete control, privacy, and no ongoing costs.

**Benefits:**
- 🔒 Complete privacy (data never leaves your machine)
- 💰 No API costs after initial setup
- 🎨 Full customization (fine-tune anything)
- ⚡ No internet required (after downloads)
- 📚 Learn how AI really works

---

### Do I need a powerful computer?

**Minimum:** You can start with:
- Any modern CPU (8+ threads)
- 8GB RAM
- No GPU required (slower but works)

**Recommended:** For best experience:
- 16GB+ RAM
- GPU with 8GB+ VRAM (RTX 3060, 4060 Ti, etc.)
- 100GB+ free storage

**Can I use CPU only?**  
Yes! Use quantized models (GGUF format) which run well on CPU. They're slower but functional.

---

### How much does it cost?

**Initial Costs:**
- Software: $0 (everything is free/open-source)
- Hardware: $0-$1500+ (depending on what you already have)

**Ongoing Costs:**
- $0 (just electricity)

**Compare to cloud:**
- OpenAI API: $0.01-0.03 per 1K tokens
- Using local: One-time hardware investment, then free forever

---

### Is it legal to use leaked models?

**LLaMA 1:** Originally leaked, legal gray area  
**LLaMA 2/3:** Officially released by Meta, fully legal  
**Mistral:** Open source, Apache 2.0 license  
**Stable Diffusion:** Open source, CreativeML license

**General rule:** Use officially released models to stay safe. Most popular models now have proper licenses.

---

## Technical Questions

### What's the difference between LLaMA, Mistral, and Phi?

**LLaMA (Meta):**
- Foundation model by Facebook/Meta
- Very strong base performance
- Most fine-tunes built on this

**Mistral (Mistral AI):**
- French AI company
- Exceptional quality for size
- Great for production use

**Phi (Microsoft):**
- Small models (1-3B parameters)
- Excellent for limited hardware
- Good for specific tasks

**Recommendation:** Start with Mistral 7B or Llama 3.2 for best balance.

---

### What format should I use? GGUF, GPTQ, AWQ?

**GGUF (llama.cpp):**
- ✅ Best for CPU inference
- ✅ Works on Apple Silicon (Mac M1/M2/M3)
- ✅ Flexible quantization levels
- 👉 Use this if you don't have a strong GPU

**GPTQ:**
- ✅ Best for NVIDIA GPUs
- ✅ Fast inference
- ❌ Requires GPU
- 👉 Use this with 8GB+ VRAM

**AWQ:**
- ✅ Newer, slightly better than GPTQ
- ✅ Lower memory usage
- ❌ Less widely supported
- 👉 Use for cutting-edge performance

**Full Precision (FP16/BF16):**
- ✅ Maximum quality
- ❌ Requires lots of VRAM (2GB per 1B parameters)
- 👉 Only if you have 24GB+ VRAM

**Recommendation:** Start with GGUF (Q4_K_M variant) - good quality, runs anywhere.

---

### How much VRAM do I need for different models?

**Rough estimates (GGUF Q4 quantization):**

| Model Size | VRAM Needed | Example Models |
|------------|-------------|----------------|
| 1-3B | 2-4GB | Phi-2, Llama 3.2 3B |
| 7B | 4-6GB | Mistral 7B, Llama 3.2 7B |
| 13B | 8-10GB | Llama 2 13B |
| 30B | 16-20GB | Mixtral 8x7B |
| 70B | 40GB+ | Llama 3.2 70B |

**Without enough VRAM?**
- Use CPU (slower)
- Use smaller models
- Use higher quantization (Q2/Q3)
- Rent cloud GPU for training

---

### What's the difference between base models and instruct models?

**Base Models:**
- Trained only on text prediction
- Complete sentences but don't follow instructions well
- Example: `llama-3.2-7b`

**Instruct Models:**
- Fine-tuned to follow instructions
- Better for chat and Q&A
- Example: `llama-3.2-7b-instruct`

**Which to use?**
- 👉 **Instruct models** for chatbots, assistants, Q&A
- 👉 **Base models** for fine-tuning your own version

---

### Can I use these models commercially?

**Check the license!**

**Commercial-Friendly:**
- ✅ Llama 2/3 (Meta Community License)
- ✅ Mistral (Apache 2.0)
- ✅ Stable Diffusion (CreativeML OpenRAIL)
- ✅ Phi (MIT)

**Research Only:**
- ❌ Some fine-tunes use non-commercial datasets
- ❌ Check model cards on Hugging Face

**Always verify the model card on Hugging Face before commercial use.**

---

## Setup & Installation

### Ollama doesn't recognize my GPU

**Windows:**
```powershell
# Check GPU is detected
nvidia-smi

# Update GPU drivers from NVIDIA website
# Restart Ollama
```

**Solution:**
1. Update NVIDIA drivers
2. Reinstall Ollama
3. Run: `ollama run llama3.2` (should show GPU usage in nvidia-smi)

---

### Docker won't start n8n services

**Common issues:**

**1. Port already in use:**
```bash
# Check what's using port 5678
netstat -ano | findstr :5678

# Change port in docker-compose.yml or stop the conflicting service
```

**2. Docker not running:**
```bash
# Windows: Open Docker Desktop
# Linux: sudo systemctl start docker
```

**3. Not enough resources:**
- Allocate more RAM to Docker (Docker Settings → Resources)
- Free up disk space

---

### Model downloads are very slow

**Solutions:**

**1. Use Ollama (handles downloads efficiently):**
```bash
ollama pull mistral
```

**2. Use huggingface-cli with resume:**
```bash
pip install huggingface-hub
huggingface-cli download TheBloke/Llama-2-7B-GGUF
```

**3. Download via browser:**
- Go to Hugging Face
- Download files manually
- Place in appropriate directory

**4. Use mirrors (if outside US/EU):**
- Some regions have Hugging Face mirrors
- Check community forums for local mirrors

---

### Stable Diffusion generates black images

**Common causes:**

**1. NSFW filter triggered:**
```
Solution: Add --no-half-vae flag in launch settings
Or: Use models with NSFW filter removed (civitai.com)
```

**2. Outdated GPU drivers:**
```
Solution: Update NVIDIA drivers
```

**3. Not enough VRAM:**
```
Solution: Generate smaller images (512x512)
Enable --lowvram flag
```

---

## Fine-Tuning Questions

### Should I fine-tune or use RAG?

**Use RAG (Retrieval-Augmented Generation) when:**
- ✅ You have lots of documents/data
- ✅ Information changes frequently
- ✅ You want to cite sources
- ✅ Lower cost/effort

**Use Fine-Tuning when:**
- ✅ You want specific tone/style
- ✅ Teaching new tasks/behaviors
- ✅ Need specialized knowledge
- ✅ Want offline capabilities

**Example:**
- Company docs → RAG
- Customer service personality → Fine-tune
- Medical knowledge base → RAG
- Specific coding style → Fine-tune

---

### How much data do I need to fine-tune?

**Rough guidelines:**

**LoRA (Recommended for beginners):**
- 100-1000 examples for simple tasks
- 1000-10000 for complex behaviors
- Quality > Quantity

**Full Fine-Tune:**
- 10,000+ high-quality examples
- Significant compute required
- Usually not needed

**DreamBooth (Images):**
- 10-20 images for a person/object
- 50-100 for concepts/styles

**Start small:** Try 100 examples, evaluate, add more if needed.

---

### My fine-tune isn't working well

**Common issues:**

**1. Overfit (memorizing):**
- Training loss keeps decreasing but quality is bad
- Solution: Stop earlier, use validation set, lower learning rate

**2. Underfit (not learning):**
- Loss not decreasing much
- Solution: More epochs, higher learning rate, more data

**3. Poor quality data:**
- Inconsistent format
- Solution: Clean and standardize your dataset

**4. Wrong hyperparameters:**
- Solution: Start with proven configurations from community

**Debug checklist:**
1. Check data quality (review 10 random examples)
2. Verify data format matches expected
3. Start with tiny dataset (10 examples) to test pipeline
4. Monitor training loss
5. Test early checkpoints

---

## Project-Specific Questions

### Can I build a ChatGPT clone?

**Yes!** Multiple approaches:

**1. Simple (Ollama + Web UI):**
```bash
# Use Ollama with web interface
ollama pull mistral
# Add Streamlit or Gradio UI
```

**2. Advanced (n8n workflow):**
- n8n chat interface
- RAG for knowledge
- Voice input/output

**3. Production (Text Generation WebUI):**
- Oobabooga supports multiple users
- API endpoints
- Extensions

**Most similar to ChatGPT:** Oobabooga Text Gen WebUI or LM Studio

---

### How do I make AI remember conversations?

**Options:**

**1. Keep conversation history:**
```python
# Store all messages in array
history = [
    {"role": "user", "content": "Hello"},
    {"role": "assistant", "content": "Hi!"},
    # ... keep building
]
```

**2. Summarization:**
```python
# After N messages, summarize older ones
# Keep recent + summary
```

**3. Vector database:**
```python
# Store past conversations in Qdrant
# Retrieve relevant past context
```

**4. Fine-tuning:**
```python
# Fine-tune on user's communication style
# Model "learns" user preferences
```

**Recommendation:** Start with #1 (simple history), add #3 (vector DB) for long-term memory.

---

### Can I run multiple models simultaneously?

**Yes, but consider VRAM:**

**With 24GB VRAM:**
- Run 2-3 small models (7B each)
- 1 medium model (13B) + 1 small (7B)

**With 8GB VRAM:**
- 1 model at a time
- Or multiple tiny models (1-3B each)

**Use Ollama:**
```bash
# Terminal 1
ollama run mistral

# Terminal 2  
ollama run codellama
# Both run on same Ollama server, managed automatically
```

---

## Performance & Optimization

### How can I make inference faster?

**Hardware:**
1. Use GPU (10-50x faster than CPU)
2. Upgrade RAM (prevent swapping)
3. Use SSD/NVMe (faster model loading)

**Software:**
1. Use quantized models (Q4_K_M good balance)
2. Reduce context length (shorter = faster)
3. Use smaller models for simple tasks
4. Enable GPU acceleration in tools

**llama.cpp optimizations:**
```bash
# Use GPU layers
./main -ngl 35  # offload 35 layers to GPU

# Multiple threads
./main -t 8     # use 8 CPU threads
```

---

### My computer freezes when generating images

**Causes:**

**1. Out of VRAM:**
```
Solution: 
- Generate smaller images
- Use --lowvram or --medvram flags
- Close other apps
```

**2. Too many background processes:**
```
Solution:
- Close browsers, apps
- Don't generate multiple images at once
```

**3. Insufficient RAM:**
```
Solution:
- Close other apps
- Increase Windows page file
- Gen one image at a time
```

**Settings to try (Stable Diffusion):**
- Steps: 20-30 (not 50+)
- Size: 512x512 (not 1024+)
- Batch: 1 (not 4+)
- Enable xFormers

---

## Error Messages

### "Model not found" errors

**Ollama:**
```bash
# List available models
ollama list

# Pull the model
ollama pull llama3.2

# Verify
ollama run llama3.2
```

**Other tools:**
- Check model path in config
- Download model from Hugging Face
- Place in correct directory

---

### "CUDA out of memory" errors

**Solutions (in order):**

1. **Close other GPU apps** (browsers, etc.)
2. **Use smaller batch size**
3. **Use quantized model** (Q4 instead of FP16)
4. **Reduce context length**
5. **Use CPU instead** (slower but works)
6. **Upgrade GPU** (if nothing else works)

**For Stable Diffusion:**
```
--lowvram      # less than 4GB VRAM
--medvram      # 4-8GB VRAM
--xformers     # efficiency boost
```

---

### "Connection refused" when using Ollama

**Solutions:**

**1. Start Ollama server:**
```bash
ollama serve
```

**2. Check if running:**
```bash
# Windows
netstat -ano | findstr :11434

# Mac/Linux
lsof -i :11434
```

**3. Firewall blocking:**
- Add exception for Ollama
- Or temporarily disable firewall to test

---

## Community & Support

### Where can I get help?

**Communities (most active to least):**
1. **r/LocalLLaMA** (Reddit) - Most active
2. **Stability AI Discord** - Image generation
3. **Oobabooga Discord** - Text generation
4. **Hugging Face Forums** - Technical discussions

**Before asking:**
1. Search for your error message
2. Check tool's GitHub Issues
3. Read the README/docs
4. Include error messages + system info

---

### How do I stay updated?

**Subscribe to:**
- r/LocalLLaMA (daily news)
- Hugging Face daily papers
- YouTube: Matthew Berman (model reviews)
- Twitter: @ollama, @stabilityai

**Check weekly:**
- Ollama library (new models)
- CivitAI (new image models)
- This repo (updates)

---

### Can I contribute to open-source models?

**Yes! Ways to help:**

**1. Create fine-tunes:**
- Share on Hugging Face
- Document training process

**2. Build applications:**
- Open-source on GitHub
- Share with community

**3. Create datasets:**
- Collect and clean data
- Share on Hugging Face

**4. Write documentation:**
- Tutorials and guides
- Improve existing docs

**5. Report issues:**
- Bug reports
- Feature requests

---

## Safety & Ethics

### Is AI-generated content detectable?

**Text:** Increasingly difficult to detect
- AI detectors have high false positive rates
- Editing makes detection harder
- Best practice: Disclose AI use when required

**Images:** Usually detectable by experts
- Artifacts, inconsistencies
- Metadata (if preserved)
- Style patterns

**Audio/Video:** Getting harder
- Deepfakes increasingly realistic
- Watermarking solutions in development

**Recommendation:** Use AI responsibly, disclose when appropriate.

---

### What are the ethical considerations?

**Privacy:**
- ✅ Local AI = your data stays private
- ⚠️ Be careful what you train on (respect copyrights)

**Bias:**
- ⚠️ Models inherit biases from training data
- 👉 Evaluate outputs critically
- 👉 Fine-tune to reduce harmful biases

**Misinformation:**
- ⚠️ AI can generate convincing false information
- 👉 Verify important facts
- 👉 Label AI-generated content

**Deepfakes:**
- ⚠️ Don't create non-consensual content
- ⚠️ Don't impersonate others
- ✅ Use for creative/educational purposes

---

### Can I use AI to write my school essays?

**Educational perspective:**

**Allowed:**
- ✅ Brainstorming ideas
- ✅ Checking grammar
- ✅ Learning concepts
- ✅ Research assistance

**Not allowed (typically):**
- ❌ Submitting AI-written work as your own
- ❌ Using AI during exams (without permission)

**Best practice:**
- Check your institution's policy
- Use AI as a learning tool, not replacement
- Always cite AI assistance if used

**Learning value:** Understanding > Completion

---

## Getting Started

### I'm completely new. Where do I start?

**Week 1 Plan:**

**Day 1-2: Install fundamentals**
```
1. Install Docker
2. Install Ollama
3. Pull a model: ollama pull llama3.2
4. Chat with it: ollama run llama3.2
```

**Day 3-4: First project**
```
1. Clone basic-chatbot template
2. Run it: python chatbot.py
3. Modify system prompt
4. Experiment with different models
```

**Day 5-6: Image generation**
```
1. Install Stability Matrix
2. Install Stable Diffusion WebUI
3. Generate first image
4. Try different prompts
```

**Day 7: Explore**
```
1. Browse RESOURCES.md
2. Join r/LocalLLaMA
3. Plan your first real project
```

---

### What should I build as my first project?

**Beginner Projects (increasing difficulty):**

**1. Personal Journal Analyzer** (Easy)
- Whisper transcribes voice notes
- LLM summarizes and finds patterns
- Save insights to database

**2. Code Commenter** (Easy-Medium)
- Reads your code files
- Adds comments explaining logic
- Helps with documentation

**3. Recipe Generator** (Medium)
- Input: Available ingredients
- Output: Recipe ideas
- Image generation for plating

**4. Study Assistant** (Medium)
- Upload textbooks/notes
- RAG for Q&A
- Quiz generation

**5. Personal AI Assistant** (Hard)
- Voice control (Whisper)
- Calendar integration
- Task management
- Email drafting

**Start small, iterate, build!**

---

## Still Have Questions?

**Can't find your answer?**

1. **Search this repo:** Use GitHub search
2. **Check main guide:** README.md has detailed explanations
3. **Ask community:** Open GitHub Discussion
4. **Report issue:** If something's broken

**We're here to help! 🚀**

---

*FAQ Last Updated: March 2026*  
*Submit additional questions via GitHub Issues*
