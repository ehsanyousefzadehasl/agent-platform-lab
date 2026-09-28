# agent-platform-lab
A small platform for running, observing, and evaluating AI coding agents through MCP tools.

The project will progressively add:

- an agent execution loop;
- repository tools exposed through MCP;
- evaluation and tracing;
- Docker packaging;
- Kubernetes deployment;
- human approval and security controls.

## Learning notes

### Unit 1: Setup and basic definition

An AI agent combines:

1. a model that selects actions;
2. instructions defining its objective and constraints;
3. tools for interacting with external systems;
4. an execution loop that observes results and chooses the next action.

MCP provides a standard interface through which applications can expose tools and
context to an AI agent.

MCP separates supplying tools and context from the model interaction itself, which is why it fits this platform design.

First interview question:

```
What distinguishes an AI agent from a normal LLM request?
```

Short answer:

```
A normal request produces a response once. An agent can iteratively select tools, observe their results, update its state, and continue until it completes a task or reaches a stopping condition.
```

### Unit 2: Installable package and CLI

**pyproject.toml** defines project metadata, dependencies, build configuration, and executable commands. The src/ layout prevents accidental imports from the repository root.

```
The [project.scripts] entry creates the agent-platform terminal command.
```

The project uses the `src/` layout so application imports come from the installed
package rather than accidentally resolving against files in the repository root.

`pyproject.toml` provides one place for package metadata, dependencies, build
configuration, test configuration, and CLI entry points.


```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e ".[dev]"
python -m pytest
agent-platform "inspect the repository"
```

In Linux/ Mac, it is different:

```
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
python -m pytest
```

Question:

```
Why use an installable package instead of running loose Python scripts?
```

Answer:

```
It provides reproducible dependencies, stable imports, testable modules, and a defined command-line interface suitable for deployment.
```