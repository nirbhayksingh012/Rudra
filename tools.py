import math
# pyrefly: ignore [missing-import]
from duckduckgo_search import DDGS

def calculate(expression: str) -> str:
    """Safely evaluate mathematical expressions using math library functions."""
    try:
        # Remove any harmful characters to make evaluation safe
        allowed_chars = "0123456789+-*/(). space"
        # Also allow standard math function names
        safe_names = {
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "sqrt": math.sqrt,
            "pi": math.pi,
            "pow": math.pow,
            "log": math.log,
        }
        
        # Clean expression
        clean_expr = "".join(c for c in expression if c in allowed_chars or c.isalpha())
        
        # Evaluate safely
        val = eval(clean_expr, {"__builtins__": None}, safe_names)
        return f"{expression} = {val}"
    except Exception as e:
        return f"Error evaluating '{expression}': {str(e)}"

def web_search(query: str) -> str:
    """Search DuckDuckGo and return a compact summary of top 3 search results."""
    try:
        # Clean query
        query = query.strip().strip('"').strip("'")
        with DDGS() as ddgs:
            results = ddgs.text(query, max_results=3)
            if not results:
                return f"No search results found for '{query}'"
            
            summary_parts = []
            for i, r in enumerate(results, 1):
                title = r.get("title", "No Title")
                snippet = r.get("body", "No Snippet")
                summary_parts.append(f"[{i}] {title}: {snippet}")
            
            return "\n\n".join(summary_parts)
    except Exception as e:
        return f"Error searching for '{query}': {str(e)}"

# Simple test if run directly
if __name__ == "__main__":
    print("Testing calculate:")
    print(calculate("sqrt(144) + 25 * 3"))
    print("\nTesting web_search:")
    print(web_search("capital of France"))
