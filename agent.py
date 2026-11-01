"""A tiny, dependency-free command-line agent."""


def respond(message: str) -> str:
    text = message.strip().lower()
    if not text:
        return "Please enter a message."
    if any(word in text for word in ("hello", "hi", "你好", "嗨")):
        return "Hello! I'm a tiny agent. Ask me about the time, or say help."
    if "help" in text or "帮助" in text:
        return "I can greet you, tell you the current local time, and repeat your message."
    if "time" in text or "时间" in text:
        from datetime import datetime
        return f"The current local time is {datetime.now().astimezone().strftime('%Y-%m-%d %H:%M:%S %Z')}"
    return f"You said: {message.strip()}"


def main() -> None:
    print("Simple Agent (type 'quit' to exit)")
    while True:
        try:
            message = input("You: ")
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break
        if message.strip().lower() in {"quit", "exit", "退出"}:
            print("Goodbye!")
            break
        print(f"Agent: {respond(message)}")


if __name__ == "__main__":
    main()
