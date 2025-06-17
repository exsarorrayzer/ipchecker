import os
import subprocess
import sys

# Fallback console output if rich isn't available
def print_message(message, title=None):
    try:
        from rich.console import Console
        from rich.panel import Panel
        console = Console()
        if title:
            console.print(Panel(message, title=title, subtitle="By Rayzer"))
        else:
            console.print(message)
    except ImportError:
        border = "=" * 50
        if title:
            print(f"\n{border}\n{title.center(50)}\n{border}")
        print(message)
        if title:
            print(f"{border}\n")

def run_setup():
    print_message("IP Lookup Tool Setup", "Starting Installation")
    
    # Create requirements.txt
    requirements = ["requests", "rich"]
    try:
        with open("requirements.txt", "w") as f:
            f.write("\n".join(requirements))
        print_message("[+] Created requirements.txt", "Setup Progress")
    except Exception as e:
        print_message(f"[!] Failed to create requirements.txt: {str(e)}", "Error")
        return

    # Install dependencies
    print_message("[*] Installing dependencies...", "Setup Progress")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print_message("[✓] Dependencies installed successfully", "Success")
    except subprocess.CalledProcessError:
        print_message("[!] Failed to install dependencies. Trying manual installation...", "Warning")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
            subprocess.check_call([sys.executable, "-m", "pip", "install", "rich"])
            print_message("[✓] Manual installation successful", "Success")
        except Exception as e:
            print_message(f"[!] Critical error during installation: {str(e)}", "Error")
            return

    # Verify setup
    print_message("[*] Verifying installation...", "Setup Progress")
    try:
        import requests
        print_message("[✓] requests module verified", "Verification")
    except ImportError:
        print_message("[!] requests module failed to install", "Error")
    
    try:
        from rich import print as rich_print
        print_message("[✓] rich module verified", "Verification")
    except ImportError:
        print_message("[!] rich module failed to install (fallback to basic output)", "Warning")

    print_message(
        "Setup completed!\n"
        "Run the tool with: python main.py\n"
        "For best experience, ensure rich is installed.",
        "Installation Complete"
    )

if __name__ == "__main__":
    run_setup()
