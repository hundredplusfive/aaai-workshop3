# 🧳 Travel Planning Committee – AI Trip Planner

## 📝 Overview

This project simulates a **Travel Planning Committee** made up of AI agents, each with a distinct personality and area of expertise. The system helps users plan a trip based on **weather conditions**, **cost breakdowns**, and **travel activities** through a natural multi-turn conversation.

---

## 🎯 Objective

Help users choose suitable travel destinations by simulating how a real travel committee might work together—offering personalized suggestions, cost breakdowns, weather info, and activity ideas.

---

## 🧠 Agents & Tool Access

| Agent  | Role / Background                  | Tools Access                         |
|--------|------------------------------------|--------------------------------------|
| Emily  | Travel budget analyst              | `cost_breakdown`, `activities`       |
| Mark   | Ex-meteorologist travel consultant | `weather`, `activities`              |
| Sara   | Adventure tour guide & backpacker  | `activities`, `cost_breakdown`       |

---

## Setup
Step 1: Add your OpenAI API Key into the file named ***.env.example***

Step 2: Rename the  ***.env.example*** file to ***.env***

Step 3: Turn off VPN

---

## Running the project

```sh
uv sync

uv run python main.py
```
Additional note: Due to some constraints/configuration of the project, 
the interaction between User and Participant is recommended to be completed within 6 exchanges.
If not, the following error/exception will be shown:
```sh
An error occurred: Recursion limit of 25 reached without hitting a stop condition. You can increase the limit by setting the `recursion_limit` config key.
For troubleshooting, visit: https://python.langchain.com/docs/troubleshooting/errors/GRAPH_RECURSION_LIMIT
Ending conversation...
```

### Prompt Tips
Your first prompt should be telling the application 1 or more of the following:
1. The number of days for the trip
2. The month to travel
3. Budget constraints

