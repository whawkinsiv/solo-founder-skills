# The matrix

Score each dimension 0–5 with the anchors in "How to judge it." Then read the directional signal for that score in the last column.

| Dimension | Weight | How to judge it (0–5) | Why it matters / directional signal |
|---|---:|---|---|
| **Interface essentiality** | **15%** | **0:** UI adds almost nothing; text/API invocation is enough. **3:** UI improves efficiency or trust. **5:** interaction with the interface *is* the product. | Highest-weight signal. Low → API/skill/agent. Medium → thin control plane/web app. High → rich web/native/desktop app. |
| **Agent substitutability** | **10%** | **0:** an agent cannot meaningfully perform the work. **3:** agent can perform parts with human interaction. **5:** a capable agent with tool access can perform essentially the whole job. | High → agent-native skill/tool/API. Low → dedicated human-facing application more justified. |
| **Visual / spatial dependence** | **10%** | **0:** nothing important is lost in text. **3:** charts/previews materially help. **5:** users must see, manipulate, arrange, compare, draw, navigate, or inspect visually. | High strongly favors rich GUI products: design, CAD, maps, dashboards, editors. |
| **Workflow ownership** | **10%** | **0:** one atomic operation. **1:** utility. **2:** task. **3:** multi-step workflow. **4:** system of record. **5:** platform/ecosystem owning a major business process. | Determines product scope: function/API → tool → SaaS → system of record → platform/ecosystem. |
| **Background / autonomous execution** | **9%** | **0:** only does something when explicitly invoked. **3:** occasional scheduled/background jobs. **5:** continuously monitors, reacts, or executes without the user present. | High → service/agent/automation infrastructure. Often means the visible UI should be only a control plane. |
| **Durable state requirement** | **8%** | **0:** stateless. **1:** current-session context only. **3:** history/settings/projects matter. **5:** persistent state is central and authoritative. | Low → website/API/skill. High → backend + accounts + database; very high can imply system-of-record SaaS. |
| **External integration dependence** | **8%** | **0:** self-contained. **2:** one optional integration. **3:** integrations materially improve value. **5:** the product fundamentally exists to interact with other systems. | High → API, connector, plugin, MCP/tool layer, integration SaaS. Can reduce need for a large proprietary UI. |
| **Device / environment dependence** | **7%** | **0:** runs equally well anywhere. **2:** browser/IDE context matters. **3:** OS/files/local compute matter. **5:** camera, GPS, sensors, Bluetooth, offline use, push, etc. are central. | Determines surface: browser extension, IDE plugin, desktop app, native mobile, hardware/software. |
| **Human judgment / intervention frequency** | **5%** | **0:** deterministic and autonomous. **2:** occasional approval. **3:** user chooses among recommendations regularly. **5:** continuous human decisions are fundamental. | Low → automation/API/agent. High → interactive app/copilot. Also determines whether approval queues or previews are necessary. |
| **Collaboration / permission complexity** | **5%** | **0:** one user, no sharing. **2:** sharing/export. **3:** teams and ownership. **5:** organizations, roles, permissions, approvals, external stakeholders. | High creates genuine SaaS complexity and usually justifies persistent UI, identity, permissions, and admin surfaces. |
| **Latency / interaction loop** | **4%** | **0:** minutes/hours/days are acceptable. **2:** seconds are desirable. **5:** continuous or near-instant feedback is necessary. | High favors interactive GUI/native/local execution. Low favors async agent, background job, API, or service. |
| **Distribution-context fit** | **4%** | **0:** users must deliberately visit a new destination. **3:** useful inside an existing workflow. **5:** value is greatest when embedded exactly where the user already works. | High → plugin, extension, skill, embedded widget, Slack bot, IDE tool. Low → standalone destination product is more plausible. |
| **Extensibility requirement** | **3%** | **0:** fixed capability. **2:** configurable. **3:** customers create workflows/templates. **5:** third parties should build extensions, apps, or integrations on top. | High → platform/API/SDK/plugin ecosystem rather than merely an application. |
| **Audit / control requirement** | **2%** | **0:** failure is trivial and reversible. **2:** history/undo helpful. **3:** approvals/logs important. **5:** consequential actions require audit trails, permissions, explanations, rollback, or compliance. | High often creates a necessary UI even for an otherwise agent-native product: logs, approvals, history, permissions, exceptions. |

## Test questions

Use one question per dimension to score consistently. Each question points back to the anchors above. It does not replace them.

1. **Interface essentiality:** "If the result arrived as plain text or an API response, what would the user lose?"
2. **Agent substitutability:** "Could a capable agent with tool access do the whole job?"
3. **Visual / spatial dependence:** "Would a text description be enough, or must users see, arrange, draw, or inspect something?"
4. **Workflow ownership:** "Is this one operation, a task, a multi-step workflow, or the system where the records of this work live?"
5. **Background / autonomous execution:** "Does anything need to happen while the user is not there?"
6. **Durable state requirement:** "If everything reset after each use, what would break?"
7. **External integration dependence:** "Take away every connection to another system. What is left?"
8. **Device / environment dependence:** "Does it need a specific place to run (a browser, an IDE, the user's own computer) or specific hardware (camera, GPS, sensors, Bluetooth, offline use, push)?"
9. **Human judgment / intervention frequency:** "How often must a person decide something while it runs?"
10. **Collaboration / permission complexity:** "How many people touch the same data, and do they need different rights?"
11. **Latency / interaction loop:** "Is it acceptable if the answer arrives in minutes or hours?"
12. **Distribution-context fit:** "Where is the user when they need this, and would they have to leave that place to use it?"
13. **Extensibility requirement:** "Will customers or third parties build on top of it?"
14. **Audit / control requirement:** "What happens if it does the wrong thing, and can it be undone?"
