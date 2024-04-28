def load_css(file_name):
    with open(file_name, "r") as f:
        return f"<style>{f.read()}</style>"
    