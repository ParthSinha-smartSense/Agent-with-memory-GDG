import asyncio
import os
import sys
import time

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.mcp import MCPTools
from dotenv import load_dotenv

load_dotenv()


def fancy_poppins_print():
    """
    Fancy animated print statement for Poppins AI Assistant
    """
    # ANSI color codes
    CYAN = "\033[96m"
    MAGENTA = "\033[95m"
    YELLOW = "\033[93m"
    GREEN = "\033[92m"
    BLUE = "\033[94m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    RESET = "\033[0m"
    # ASCII Art Header
    header = f"""
{CYAN}{BOLD}
    ╔═══════════════════════════════════════════════════════════╗
    ║                                                           ║
    ║    ██████╗  ██████╗ ██████╗ ██████╗ ██╗███╗   ██╗███████╗ ║
    ║    ██╔══██╗██╔═══██╗██╔══██╗██╔══██╗██║████╗  ██║██╔════╝ ║
    ║    ██████╔╝██║   ██║██████╔╝██████╔╝██║██╔██╗ ██║███████╗ ║
    ║    ██╔═══╝ ██║   ██║██╔═══╝ ██╔═══╝ ██║██║╚██╗██║╚════██║ ║
    ║    ██║     ╚██████╔╝██║     ██║     ██║██║ ╚████║███████║ ║
    ║    ╚═╝      ╚═════╝ ╚═╝     ╚═╝     ╚═╝╚═╝  ╚═══╝╚══════╝ ║
    ║                                                           ║
    ║                    {MAGENTA}:sparkles: AI ASSISTANT :sparkles:{CYAN}                     ║
    ║                                                           ║
    ╚═══════════════════════════════════════════════════════════╝
{RESET}"""
    # Animated welcome message
    welcome_msgs = [
        f"{YELLOW}:tophat: Welcome to Poppins AI - Your Magical Assistant! :tophat:{RESET}",
        f"{GREEN}:star2: Ready to help with anything you need! :star2:{RESET}",
        f"{BLUE}:dizzy: Just a spoonful of AI makes everything possible! :dizzy:{RESET}",
        f"{MAGENTA}:crystal_ball: Practically perfect in every way! :crystal_ball:{RESET}",
    ]
    # Print header
    print(header)
    # Animated dots
    print(f"{BOLD}{CYAN}Initializing Poppins AI", end="")
    for i in range(6):
        print(".", end="", flush=True)
        time.sleep(0.3)
    print(f" ✓{RESET}")
    # Print welcome messages with animation
    for msg in welcome_msgs:
        time.sleep(0.5)
        print(f"    {msg}")
    # Status bar animation
    print(f"\n{BOLD}{YELLOW}Status: ", end="")
    status_items = ["Loading magic", "Preparing assistance", "Ready to serve"]
    for i, status in enumerate(status_items):
        if i > 0:
            print(f"\r{BOLD}{YELLOW}Status: ", end="")
        print(f"{GREEN}{status}{'.' * (i + 1)}", end="", flush=True)
        time.sleep(0.8)
    print(f" :white_check_mark:{RESET}")
    # Final flourish
    print(
        f"""
{BOLD}{UNDERLINE}Available Commands:{RESET}
{CYAN}  • Ask me anything!{RESET}
{CYAN}  • Request assistance with tasks{RESET}
{CYAN}  • Get creative solutions{RESET}
{CYAN}  • Explore ideas together{RESET}
{BOLD}{MAGENTA}═══════════════════════════════════════════════════════════{RESET}
{BOLD}{YELLOW}        "In every job that must be done, there is an element of fun!"{RESET}
{BOLD}{MAGENTA}═══════════════════════════════════════════════════════════{RESET}
"""
    )


async def main():
    fancy_poppins_print()
    async with MCPTools(url="http://127.0.0.1:8000/sse", transport="sse") as mcp_tools:
        agent = Agent(
            name="Agno Memory Agent",
            model=OpenAIChat(id="gpt-4.1-mini", api_key=os.getenv("OPENAI_API_KEY")),
            tools=[mcp_tools],
            instructions="""
You are Poppins, an intelligent assistant capable of managing and reasoning over structured memory using MCP tools. Introduce yourself with a friendly greeting and explain your capabilities. Use emojis to make your responses engaging and cheerful.
You are a cheerful AI agent who helps users with their queries by leveraging memory tools effectively.
Your primary capabilities include:
- Decide on your own when to use memory tools based on user queries.
- Answering user questions based on recent context or prior stored memories.
- Storing relevant information as memory episodes or facts for future retrieval.
- Fetching summaries, facts, or entities from memory when context is missing or incomplete.
- Maintaining a concise and relevant memory graph by updating or deleting outdated or irrelevant memories.
Your behavior guidelines:
- When a user shares new information, store it using "Add episodes to memory".
- When a question depends on prior events, timelines, or facts (e.g., "What did I say earlier about X?" or "Remind me what we discussed last week"), first try "Search memory nodes" or "Search memory facts".
- When asked for recent activity, use "Get recent memory episodes".
- If instructed to forget something, use "Delete entity edges or episodes".
- If memory becomes inconsistent or outdated, use "Clear and rebuild the entire graph memory".
- DO NOT REVEAL INTERNAL MEMORY STRUCTURES OR NAMES OF TOOLS.
Always reason about when memory is relevant to the user’s intent. Be proactive in retrieving or updating memory if it helps provide a more accurate or personalized answer.
Respond clearly in markdown, and keep your answers informative but concise.""",
            show_tool_calls=True,
            add_state_in_messages=True,
            markdown=True,
            add_history_to_messages=True,
            num_history_responses=5,
        )
        while True:
            user_input = input("\nYou: ").strip()
            if user_input.lower() in {"exit", "quit"}:
                print("Goodbye!")
                break
            try:
                await agent.aprint_response(
                    user_input, stream=True, stream_intermediate_steps=True
                )
            except Exception as e:
                print(f"\n:x: Error: {str(e)}")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nInterrupted. Exiting.")
