# Enterprise Ops Track - MASTER CLASS 2

## Demo 1: Convert a runbook into an automation plan

Objective: Transform operational prose into a specification that can be implemented and tested.

Files: 
- `Runbook_Disk_Utilization_Exercise.docx `
- `Runbook_Automation_Control_Checklist.docx`

**Prompt:**

Using the supplied Disk Utilization Runbook and Runbook Automation Control Checklist, produce an automation specification.

For each step, identify:
- Input or evidence required
- Documented condition or rule
- Proposed action
- Whether the action changes system state
- Approval requirement
- Expected postcondition
- Audit event
- Failure handling and stop/escalate condition

Separate read-only checks from state-changing actions. Do not invent thresholds, treat candidate files as automatically approved for deletion, or assume that archiving files resolves the disk-utilization incident.

Default to a dry-run design. Identify any missing operational rules that would require an owner to clarify them before implementation.

## Demo 2: Review the Python automation script

Objective: Use GitHub Copilot to review a real script against the operational specification.

Files: 
- `runbook_automation_starter.py`
- `Runbook_Disk_Utilization_Exercise.docx`
- `Runbook_Automation_Control_Checklist.docx`

Open the script in VS Code and ask Copilot to:
- Explain the execution flow.
- Identify path-confinement and file-selection risks.
- Review dry-run behaviour and the --approve gate.
- Check destination collision handling.
- Inspect audit logging, error handling and postcondition validation.
- Identify idempotency limitations and missing tests.

Ask it to classify findings as defects, residual risks or design decisions requiring clarification.

**Important**: The supplied script is a teaching example. It defaults to dry-run and archives eligible old .log files in the synthetic folder. It is not production-ready, and the --approve flag is not a substitute for enterprise change authorization.

**Prompt:**
Act as a senior Site Reliability Engineer (SRE) and Python code reviewer specializing in safe operational automation.

Review runbook_automation_starter.py against the requirements in Runbook_Disk_Utilization_Exercise.docx and Runbook_Automation_Control_Checklist.docx.

This is a static code review. Do not execute the script, move files, modify the code, or access any real operational environment.

I. Explain the implementation
Summarize:
- The script's execution flow.
- How it identifies candidate log files.
- What happens in dry-run mode.
- What changes when --approve is supplied.
- How it records audit information and verifies file movement.

Distinguish what the code actually does from what its messages claim.

II. Review operational safety
Assess each of the following areas:
1.	Path confinement: Can file operations escape the supplied sample_server directory? Examine path resolution, symbolic links, and the paths passed to file operations.
2.	Candidate selection: Are only eligible .log files older than the configured age selected? Are age thresholds validated correctly?
3.	Dry-run behaviour: Does running without --approve avoid moving files? Identify any other filesystem changes that still occur.
4.	Approval gate: Is the flag sufficient for real production authorization? What additional controls would be required in a real environment?
5.	Destination collisions: What happens if a file with the same name already exists in the archive?
6.	Execution and verification: Does the script independently verify that each move succeeded? What happens if verification fails?
7.	Audit logging: What events are recorded? Could logging fail, omit useful evidence, or expose sensitive information?
8.	Error handling: Does the script stop safely when an operation fails? Are partial results and recovery needs clear?
9.	Idempotency and restart behaviour: What happens when the script is run repeatedly or after a partial failure?
10.	Operational outcome: Does the script establish that disk utilization has decreased or that the incident is resolved?

III. Report findings
For each finding, provide:
- Severity: Critical, High, Medium, Low, or Informational.
- Relevant function or code fragment.
- The observed behaviour.
- Potential operational consequence.
- A recommended correction or additional control.
- Whether the finding is a confirmed code issue, a residual risk, or a design decision requiring clarification.

Do not label a theoretical possibility as a confirmed vulnerability without evidence from the code.

IV. Evaluate against the runbook
Identify:
- Requirements implemented correctly.
- Requirements only partially implemented.
- Requirements not implemented.
- Assumptions that the runbook does not authorize.
- Conditions under which the script should stop and escalate rather than continue.

V. Recommend tests
Propose unit tests for:
- Invalid age thresholds.
- Paths outside the exercise root.
- Dry-run with no file movement.
- Recent files and non-log files.
- Existing destination filenames.
- Successful file movement and postcondition verification.
- Permission errors and partial failures.
- Repeated execution and restart behaviour.

For each test, state the setup, expected result, and control it verifies.

VI. Final assessment
Conclude with:
1.	The five most important findings, ranked by severity.
2.	The changes required before this remains a safe local training exercise.
3.	The additional controls and approvals required before adapting the design for a real operational environment.

Do not modify the file or claim that tests have been executed. 
Keep recommendations proportionate to the supplied code and documents.
Clearly distinguish code-review evidence from assumptions and recommendations.

## Demo 3: Controlled runbook execution

Objective: Show the difference between generating an action plan, approving a local exercise action, and verifying the result.

Use: synthetic `sample_server` folder.

_*To change date of files:*_

$NewDate = Get-Date -Year 2026 -Month 8 -Day 10 -Hour 9 -Minute 30 -Second 0
Set-ItemProperty -Path ".\rotation.log" -Name LastWriteTime -Value $NewDate


**First run the dry-run:**
`python runbook_automation_starter.py --older-than-days 30`

Inspect the candidate list and audit log. The script should not move any files in this mode.
If demonstrating approved mode, first confirm that the workspace is the supplied synthetic exercise folder and that the plan is understood. Then run:

`python runbook_automation_starter.py --older-than-days 30 --approve`

The approved exercise moves eligible files into the local archive directory, rather than deleting them.

Afterward, check:
- Was each moved file found in the archive?
- Is it absent from the original logs directory?
- Were any files skipped because the destination already existed?
- Was an audit record written?
- What still needs independent verification?


