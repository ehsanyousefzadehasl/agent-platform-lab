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

