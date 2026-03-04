# Example Projects

This directory contains example projects and case studies mentioned in the main guide.

---

## 📁 Project Structure

```
projects/
├── 01-wardrobe-analyzer/         # AI Wardrobe Analysis
├── 02-roast-master/              # Adversarial Training Bot
├── 03-medical-communication/     # Soft Skills for Doctors
├── 04-copilot-alternative/       # Local Code Assistant
├── 05-ekg-analyzer/              # Healthcare EKG Analysis
├── 06-clash-royale-ai/           # (Failed project - lessons learned)
└── templates/                    # Starter templates
```

---

## 🎯 Complete Projects

### 1. AI Wardrobe Analyzer

**Path**: `01-wardrobe-analyzer/`

**Description**: Analyze clothing items and get outfit recommendations

**Tech Stack**:
- Vision model (LLaVA/CLIP)
- Ollama (Mistral)
- PostgreSQL
- Qdrant

**Status**: ✅ Complete with examples

---

### 2. The Roast Master

**Path**: `02-roast-master/`

**Description**: Adversarial AI for resilience training

**Tech Stack**:
- Fine-tuned Mistral 7B
- Custom LoRA
- Safety mechanisms

**Status**: ✅ Complete with ethical guidelines

---

### 3. Medical Communication Trainer

**Path**: `03-medical-communication/`

**Description**: Practice empathy and patient communication for medical professionals

**Tech Stack**:
- Mistral-based fine-tune
- Scenario database
- Evaluation metrics

**Status**: ✅ Complete with scenarios

---

### 4. Local Copilot Alternative

**Path**: `04-copilot-alternative/`

**Description**: Free local code assistant with Continue + Ollama

**Tech Stack**:
- Ollama (DeepSeek-Coder)
- Continue VS Code extension
- Custom configurations

**Status**: ✅ Complete setup guide

---

### 5. EKG Analyzer

**Path**: `05-ekg-analyzer/`

**Description**: Healthcare application for EKG analysis

**Tech Stack**:
- ResNet CNN model
- Medical datasets (PTB-XL)
- Safety & compliance features

**Status**: ✅ Research prototype

---

### 6. Clash Royale AI (Learning from Failure)

**Path**: `06-clash-royale-ai/`

**Description**: Attempted game strategy AI - failed but educational

**Status**: ❌ Failed - comprehensive lessons learned document

---

## 📋 Project Templates

### Path: `templates/`

Ready-to-use templates for common AI projects:

1. **basic-chatbot**: Simple conversational AI
2. **rag-system**: Document Q&A with RAG
3. **image-classifier**: Fine-tune image classification
4. **text-classifier**: Sentiment/category classification
5. **voice-assistant**: Whisper + LLM + TTS pipeline

---

## 🚀 Using These Projects

### Getting Started

1. **Choose a project**:
   ```bash
   cd projects/01-wardrobe-analyzer
   ```

2. **Read the README**:
   - Each project has its own README
   - Installation instructions
   - Usage examples
   - Configuration options

3. **Install dependencies**:
   ```bash
   # Usually:
   pip install -r requirements.txt
   # Or follow project-specific instructions
   ```

4. **Run the project**:
   ```bash
   # Follow project README
   python main.py
   # Or use Docker
   docker-compose up
   ```

---

## 📚 Learning Path

### Beginner
Start with templates:
1. `basic-chatbot` - Learn LLM integration
2. `text-classifier` - Understand fine-tuning basics

### Intermediate
Move to complete projects:
1. `wardrobe-analyzer` - Multi-component system
2. `copilot-alternative` - Dev tool integration

### Advanced
Challenge yourself:
1. `medical-communication` - Specialized domain
2. `ekg-analyzer` - Computer vision + healthcare
3. Build your own inspired by these

---

## 🤝 Contributing Projects

Have a project built with local AI? Share it!

**Requirements**:
- Clear README with setup instructions
- Requirements file or environment spec
- Example usage
- Appropriate licensing

**Submit**:
1. Fork this repo
2. Add your project to `projects/`
3. Update this index
4. Create pull request

---

## 📖 Project Documentation Template

Each project should include:

```markdown
# Project Name

## Overview
Brief description and use case

## Tech Stack
- Model: [model name]
- Framework: [framework]
- Additional tools

## Installation
Step-by-step setup

## Usage
How to run and use

## Examples
Screenshots, sample outputs

## Lessons Learned
What worked, what didn't

## Future Improvements
Next steps

## License
Project license
```

---

## 🔧 Common Setup

Most projects use:
- **Python 3.9+**
- **Ollama** for LLMs
- **PostgreSQL** for data
- **n8n** for workflows (optional)

**Universal Prerequisites**:
```bash
# Python
python --version  # 3.9+

# Ollama
ollama --version

# Docker (if needed)
docker --version
```

---

## 📊 Project Complexity

| Project | Complexity | Time | Prerequisites |
|---------|-----------|------|---------------|
| Templates | ⭐ Easy | 1-2 hours | Python basics |
| Wardrobe Analyzer | ⭐⭐ Medium | 1 day | LLM experience |
| Copilot Alternative | ⭐⭐ Medium | 2-4 hours | VS Code |
| Roast Master | ⭐⭐⭐ Medium-Hard | 2-3 days | Fine-tuning |
| Medical Comm | ⭐⭐⭐ Medium-Hard | 3-5 days | Domain knowledge |
| EKG Analyzer | ⭐⭐⭐⭐ Hard | 1-2 weeks | ML/CV experience |

---

## 💡 Tips for Success

1. **Start Simple**: Begin with templates before complex projects
2. **Read Thoroughly**: Each project has detailed documentation
3. **Test Incrementally**: Don't try to run everything at once
4. **Ask for Help**: Use community resources (see RESOURCES.md)
5. **Document Changes**: Keep notes on what you modify
6. **Share Learnings**: Contribute back to the project

---

## 🎓 What You'll Learn

By working through these projects:

✅ **Technical Skills**:
- LLM integration and fine-tuning
- Vector databases and RAG
- Image generation and training
- Multi-modal AI systems
- Production deployment

✅ **Best Practices**:
- Project structure
- Error handling
- Testing and validation
- Documentation
- Ethical considerations

✅ **Problem Solving**:
- Debugging AI issues
- Performance optimization
- Resource management
- User experience design

---

## 📝 Notes

**Important**:
- Projects are educational examples
- Medical/healthcare projects: Research only, not for clinical use
- Follow all ethical guidelines
- Respect privacy and data protection

**Disclaimers**:
- Projects provided as-is
- Test thoroughly before any production use
- Adapt to your specific needs
- Check licenses for all components

---

## 🔗 Related Resources

- [Main Guide](../README.md)
- [Quick Start](../QUICKSTART.md)
- [Resources](../RESOURCES.md)

---

**Happy Building! 🚀**

*Each project represents real-world applications of local AI*
