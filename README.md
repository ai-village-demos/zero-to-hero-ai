# Zero to Hero with ChatGPT API and Python

A 2 hour workshop given in the [AI Village](https://www.cactuscon.com/villages#block-yui_3_17_2_1_1704407426583_5547) at [CactusCon 12](https://www.cactuscon.com/cc12-schedule).

Time: **2:00 pm - 4:00 pm on Friday and Saturday**<br>
Presenters: **conf1ck3r** and **Elio Grieco**

Looking for a way to break into the world of AI agents without getting overwhelmed? This hands-on session aims to teach you how to build your own AI agents from scratch using the OpenAI API and Python. The workshop emphasizes practical skills and is geared towards beginners to guide you in API usage, scripting, and web interfaces to help you boost your productivity.

Throughout the workshop, you'll build a local chatbot, craft a web application for analyzing exploit code, and develop a script that interacts with the Malware Bazaar API to gather intelligence and create informative presentations. By the end, you'll have hands-on experience in applying these skills to real-world scenarios and a solid understanding of OpenAI API and Python scripting. This workshop is an ideal starting point for industry beginners, especially Windows users, providing the foundational knowledge needed to embark on a journey in AI agent development with clarity and confidence.

## Workshop Overview

This is a basic overview of the exercises we'll cover in this workshop and what concepts will be explored during each:

0. Tooling
    - Installing Python
    - Adding dependencies
    - Alternate/Bonus: Installing [AIChat](https://github.com/sigoden/aichat): A Rust based app to use LLMs from the terminal.
1. Basic Prompts of LLMs
    - What is an LLM?
    - What is a prompt?
    - What is a good prompt?
2. Prompt Engineering
    - Refining prompts
    - Chain of thought reasoning
3. Input and Output Guidance and Data Formats
    - Parsing sloppy input data
    - Output in specific formats like JSON, CSV
4. System Prompts
    - If you had an intern, what would you want them to do?
    - Creating a good system prompt
    - Using data formats e.g. markdown
5. Code Generation
    - Cli chains
    - Explaining them
    - Writing Code in Python
6. Analyzing a GitHub Repo For Vulnerabilities
    - Creating snort rules for POC expolits on GitHub
    - Finding vulnerabilities in files from GitHub repos
7. Malware analysis via Malware Bazaar API
8. STRIDE Threat Modeling
    - What is STRIDE
9. Text Summarization
    - How to summarize text
    - Modifying the length of the summary

## Advice

The sheer amount and pace of research in this field is astounding. Keeping up with even 10% of what is released every week is nearly impossible, even for those working in the field.

Given this pace, it's important to take a pragmatic, and goal focused approach to learning about AI. Decide what you would like to accomplish, and focus your research toward that goal.

## Exercises

### 0. Tooling

In order to use any technology, there is usually common tooling that must be installed.

For this workshop we'll be using:

- Python
- OpenAI libraries
- Streamlit

Alternately, if you cannot get those to install there is [AIChat](https://github.com/sigoden/aichat), a simple Rust CLI app that can be installed by just dropping the executable into your path. It will ask for the `OPENAI_API_KEY` on the first run and automatically create a configuration file.

Some of the system prompt concepts that we will be covering later in the workshop can be emulated using [AIChat's roles](https://github.com/sigoden/aichat?tab=readme-ov-file#roles) feature. Refining and working with prompts can be accomplished via [sessions](https://github.com/sigoden/aichat?tab=readme-ov-file#session---context-aware-conversation).
