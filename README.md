# Blog Creator with CrewAI

This project creates AI-generated blog posts by researching content from YouTube channels and then writing engaging blog articles based on that research. It uses CrewAI to orchestrate a team of AI agents and OpenAI models to power the language capabilities.

## 🚀 Features

- 🤖 Multi-agent system powered by CrewAI
- 🔍 Research agent that can search YouTube channels for content
- ✍️ Writing agent that creates complete blog posts
- 🧠 Powered by OpenAI's powerful language models
- 📝 Outputs publication-ready blog posts in markdown format

## 📋 Prerequisites

- Python 3.8+
- OpenAI API key
 

## 🧩 Project Structure

```
blog-with-crewai/
├── crew.py           # Main entry point - configures and runs the crew
├── agents.py         # Defines AI agents (researcher and writer)
├── tasks.py          # Defines tasks for agents to complete
├── tools.py          # Custom tools used by agents (YouTube search)
├── requirements.txt  # Project dependencies
└── README.md         # This file
```

## 🚀 Usage

Run the main script to generate a blog post:

```bash
python crew.py
```

By default, this will:
1. Research AI and ML content from Krish Naik's YouTube channel
2. Generate a blog post based on the research
3. Output the completed blog post

## ⚙️ Configuration

You can customize the project by modifying these files:

- `tools.py`: Change the YouTube channel or add additional research tools
- `agents.py`: Modify agent roles, goals, or the OpenAI model being used
- `tasks.py`: Change the blog topic or output format requirements


## 📝 Example Output

The system will produce a markdown blog post that can be directly published or further edited as needed.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 🙏 Acknowledgements

- [CrewAI](https://github.com/joaomdmoura/crewAI) for the multi-agent framework
- [Krish Naik](https://www.youtube.com/@krishnaik06) for the educational YouTube content used for research

## Author
**Likith Sagar**