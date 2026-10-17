"""Original course notes and command references linked to IBM Redbooks chapters."""

REDBOOK_VOL1 = "https://www.redbooks.ibm.com/redbooks/pdfs/sg246981.pdf"
REDBOOK_VOL1_ABSTRACT = "https://www.redbooks.ibm.com/abstracts/sg246981.html"
REDBOOK_VOL2 = "https://www.redbooks.ibm.com/redbooks/pdfs/sg246982.pdf"
REDBOOK_VOL2_ABSTRACT = "https://www.redbooks.ibm.com/abstracts/sg246982.html"

UNITS = [
    {
        "id": "tso-ispf-jcl-sdsf",
        "title": "TSO/E, ISPF, JCL, and SDSF",
        "part": "Foundations · ABCs Volume 1, Chapter 3",
        "source": "ABCs of z/OS System Programming, Volume 1, Chapter 3",
        "page": 41,
        "url": f"{REDBOOK_VOL1}#page=41",
        "summary": (
            "TSO/E supplies interactive command access; ISPF provides panel-driven "
            "editing and utilities; JCL describes batch work to JES; SDSF displays "
            "jobs and spool when your site grants access. These are related tools, "
            "not interchangeable interfaces. This simulator accepts a small, "
            "documented command subset and never connects to a host."
        ),
        "objectives": [
            "Distinguish TSO commands, ISPF panels, JCL statements, and JES/SDSF.",
            "Identify JOB, EXEC, and DD statements in a small job.",
            "Use the simulator's HELP, TIME, LISTCAT, LISTDS, ISPF, and SDSF examples.",
        ],
        "practice": "Explain what happens from editing JCL in ISPF to reviewing completed job output in SDSF.",
        "answer": (
            "The user edits JCL, submits it to JES, JES converts and selects it, "
            "the initiator runs eligible steps, and output is held/routed according "
            "to the installation's JES setup. SDSF can display job state and spool "
            "if the user's authorization permits it. Exact workflow varies by site."
        ),
    },
    {
        "id": "implementation",
        "title": "Implementation and daily system programming",
        "part": "Chapter 1 · System implementation",
        "source": "ABCs of IBM z/OS System Programming, Volume 2, Chapter 1",
        "page": 15,
        "url": f"{REDBOOK_VOL2}#page=15",
        "summary": (
            "System implementation is planned work: understand service and capacity "
            "needs, install and customize components, define operational procedures, "
            "and manage change. Routine work includes reviewing system health, "
            "messages, service levels, operational records, backups, and maintenance "
            "windows. Treat configuration changes as controlled changes with "
            "validation and recovery plans."
        ),
        "objectives": [
            "Separate installation, customization, migration, and daily operations.",
            "Recognize why naming, security, availability, and backout planning matter.",
            "Locate SYSLOG, SMF, and LOGREC in a diagnostic workflow.",
        ],
        "practice": "A planned PARMLIB change is ready. List a safe pre-change, change, and post-change checklist.",
        "answer": (
            "Confirm the approved change and target system; validate member syntax "
            "and references; identify activation/restart requirements; preserve the "
            "current version; schedule and communicate; use a test system or change "
            "window; capture console/system evidence; verify behavior; and retain a "
            "tested backout path."
        ),
    },
    {
        "id": "parmlib-ipl",
        "title": "PARMLIB, system initialization, and IPL",
        "part": "Chapter 1 · PARMLIB and initialization",
        "source": "ABCs of IBM z/OS System Programming, Volume 2, Chapter 1",
        "page": 17,
        "url": f"{REDBOOK_VOL2}#page=17",
        "summary": (
            "PARMLIB members supply initialization and subsystem parameters. "
            "The selected LOADxx and IEASYSxx choices participate in the IPL path; "
            "other members configure functions and subsystems. An IPL is a controlled "
            "system initialization, not merely a reboot button. Validate the intended "
            "load parameters, data sets, console messages, subsystem startup, and "
            "service readiness with the installation runbook."
        ),
        "objectives": [
            "Describe the role of PARMLIB members and system symbols.",
            "Explain at a high level how IPL selection leads into initialization.",
            "Distinguish an operator DISPLAY from a configuration-changing command.",
        ],
        "practice": "Use the simulator's D IPLINFO and D PARMLIB examples; identify what each can and cannot prove.",
        "answer": (
            "D IPLINFO shows illustrative information about the current IPL; D "
            "PARMLIB shows illustrative selected parameter sources. Neither validates "
            "every setting, proves application readiness, or changes configuration."
        ),
    },
    {
        "id": "catalog-smf-logs",
        "title": "Catalogs, SMF, LOGREC, and SYSLOG",
        "part": "Chapter 1 · System data and records",
        "source": "ABCs of IBM z/OS System Programming, Volume 2, Chapter 1",
        "page": 23,
        "url": f"{REDBOOK_VOL2}#page=23",
        "summary": (
            "Catalogs help locate data sets; they are not the data sets themselves. "
            "SMF records selected system and product activity for accounting, "
            "auditing, and analysis according to configuration. LOGREC retains "
            "hardware/software error records; SYSLOG is the system log of messages. "
            "Preservation, retention, access, and interpretation follow site policy."
        ),
        "objectives": [
            "Tell a catalog lookup apart from reading a data set.",
            "Explain the distinct roles of SMF, LOGREC, and SYSLOG.",
            "Use timestamps and identifiers to correlate operational evidence.",
        ],
        "practice": "An application reports a failure at 10:15. Which evidence sources would you correlate first?",
        "answer": (
            "Start with the application/job output and timestamps; correlate SYSLOG "
            "messages, relevant SMF records if configured and authorized, and LOGREC "
            "records for related errors. Preserve evidence and follow the site's "
            "diagnostic and privacy procedures."
        ),
    },
    {
        "id": "subsystems-ssi",
        "title": "Subsystems and the subsystem interface",
        "part": "Chapter 2 · Subsystem concepts",
        "source": "ABCs of IBM z/OS System Programming, Volume 2, Chapter 2",
        "page": 33,
        "url": f"{REDBOOK_VOL2}#page=33",
        "summary": (
            "A subsystem provides a defined set of services within z/OS. The "
            "subsystem interface (SSI) lets eligible programs request services "
            "through established interfaces. Subsystem identity, initialization, "
            "registration, and dependencies must agree with system configuration. "
            "Use read-only displays for diagnosis; do not infer that starting or "
            "changing a subsystem is safe from a sample command."
        ),
        "objectives": [
            "Define subsystem and SSI without equating SSI to a product itself.",
            "Recognize that subsystem order and dependencies can matter.",
            "Know when an operator action requires an authorized change procedure.",
        ],
        "practice": "A subsystem is not available after IPL. Name three configuration or operational areas to verify.",
        "answer": (
            "Check the approved subsystem definitions/initialization parameters, "
            "startup ordering and dependencies, and console/JES/system messages. "
            "Confirm the configured subsystem identifier and site runbook; escalate "
            "rather than changing live definitions ad hoc."
        ),
    },
    {
        "id": "jes-job-flow",
        "title": "JES job lifecycle and output",
        "part": "Chapter 3 · JES2 and JES3 job management",
        "source": "ABCs of IBM z/OS System Programming, Volume 2, Chapter 3",
        "page": 39,
        "url": f"{REDBOOK_VOL2}#page=39",
        "summary": (
            "JES receives batch jobs, processes JCL, queues work, and manages "
            "spool/output. Job lifecycle and controls differ between JES2 and JES3 "
            "and between installations. A job's completion code is only one clue: "
            "review JES messages, JCL, step messages, program output, and site "
            "routing before deciding whether the work succeeded."
        ),
        "objectives": [
            "Describe submission, conversion/interpretation, execution, and output at a high level.",
            "Distinguish job status from successful business results.",
            "Use SDSF-style displays as a viewing workflow, subject to authorization.",
        ],
        "practice": "A job ends with a non-zero return code. List the spool sections and evidence to inspect.",
        "answer": (
            "Inspect JESMSGLG for JES status/messages, JESJCL for submitted JCL and "
            "resolved procedures, JESYSMSG for allocation/execution messages, each "
            "step's SYSOUT and application output, and any installation-specific "
            "logs. Interpret the code using the program's documented meaning."
        ),
    },
    {
        "id": "jes-commands",
        "title": "JES operator commands and controls",
        "part": "Chapter 3 · JES operations",
        "source": "ABCs of IBM z/OS System Programming, Volume 2, Chapter 3",
        "page": 51,
        "url": f"{REDBOOK_VOL2}#page=51",
        "summary": (
            "JES operator commands are subsystem-specific and run in an authorized "
            "operator context; they are not ordinary TSO commands. JES2 uses a "
            "dollar-sign command family, while JES3 syntax differs. This course "
            "recognizes a small read-only illustrative subset only. Never copy "
            "examples into a production console without checking the installed "
            "release's command reference and local procedures."
        ),
        "objectives": [
            "Recognize the JES2 `$` command family in examples.",
            "Understand that JES3 syntax and commands are different.",
            "Separate display/inspection from hold, cancel, purge, or modify actions.",
        ],
        "practice": "Classify `$D JOB` and `$C JOB` as read-only or state-changing, and explain the distinction.",
        "answer": (
            "`$D JOB` is a JES2 display-style example; `$C JOB` is a cancel command "
            "and changes work state. The simulator never executes either against JES."
        ),
    },
    {
        "id": "jes3",
        "title": "JES3 job management and installation differences",
        "part": "Chapter 3 · JES3 comparison",
        "source": "ABCs of IBM z/OS System Programming, Volume 2, Chapter 3",
        "page": 39,
        "url": f"{REDBOOK_VOL2}#page=39",
        "summary": (
            "JES3 and JES2 both support z/OS batch job management, but their "
            "architecture, scheduling, configuration, and operator interfaces are "
            "not identical. Commands and procedures must match the JES product and "
            "release actually installed. This course does not invent a JES3 "
            "operator command; use the linked chapter and current product manuals."
        ),
        "objectives": [
            "Recognize that JES3 is a distinct job-entry subsystem.",
            "Avoid transferring JES2 commands or procedures to JES3 without verification.",
            "Trace the batch-job lifecycle using installation-specific JES evidence.",
        ],
        "practice": "A runbook contains a JES2 `$D` command, but the system runs JES3. What should you do?",
        "answer": (
            "Do not issue it. Consult the JES3 command reference for the installed "
            "release and local operating procedures, then use an authorized console "
            "and change controls appropriate to the action."
        ),
    },
    {
        "id": "lpa-lnklst-apf",
        "title": "LPA, LNKLST, APF, LLA, and VLF",
        "part": "Chapter 4 · Libraries and authorization",
        "source": "ABCs of IBM z/OS System Programming, Volume 2, Chapter 4",
        "page": 125,
        "url": f"{REDBOOK_VOL2}#page=125",
        "summary": (
            "LPA contains modules mapped for system-wide use; LNKLST defines "
            "libraries searched for program modules; APF authorization is a security "
            "attribute for trusted libraries/modules. LLA and VLF support library "
            "management and directory/data access. These mechanisms affect system "
            "integrity: library content, concatenation order, authorization, and "
            "refresh procedures require strict controls."
        ),
        "objectives": [
            "Explain LPA and LNKLST at a high level.",
            "Explain why APF authorization is security-sensitive.",
            "Recognize the roles of LLA and VLF without treating them as interchangeable.",
        ],
        "practice": "Why must APF library changes be reviewed more carefully than ordinary data-set updates?",
        "answer": (
            "Authorized code can receive elevated system privileges. A library "
            "change can therefore affect system integrity, so ownership, access, "
            "content, concatenation, change approval, and verification must be "
            "controlled."
        ),
    },
    {
        "id": "smpe",
        "title": "SMP/E zones, SYSMODs, and maintenance",
        "part": "Chapter 5 · SMP/E for z/OS",
        "source": "ABCs of IBM z/OS System Programming, Volume 2, Chapter 5",
        "page": 159,
        "url": f"{REDBOOK_VOL2}#page=159",
        "summary": (
            "SMP/E records software inventory and maintenance in CSI zones. The "
            "global zone tracks received SYSMODs and related metadata; target zones "
            "describe installed target libraries; distribution zones describe the "
            "distribution libraries. A SYSMOD can be a function, PTF, APAR, or "
            "USERMOD. RECEIVE, APPLY CHECK, APPLY, and ACCEPT are separate phases; "
            "a USERMOD is a valid package with MCS and element content, not a "
            "placeholder identifier."
        ),
        "objectives": [
            "Distinguish global, target, and distribution zones.",
            "Explain RECEIVE, APPLY CHECK, APPLY, and ACCEPT at a high level.",
            "Identify requisites and HOLDDATA as items to review before installation.",
        ],
        "practice": "A sandbox USERMOD was received. Give the safest next SMP/E step and explain what it does not do.",
        "answer": (
            "Inspect the received SYSMOD and run APPLY CHECK for the intended "
            "target zone. It checks applicability and reports conditions; it does "
            "not install the change. Review requisites, HOLDDATA, reports, and "
            "backout controls before an authorized APPLY."
        ),
    },
    {
        "id": "language-environment",
        "title": "Language Environment (LE)",
        "part": "Chapter 6 · Runtime architecture",
        "source": "ABCs of IBM z/OS System Programming, Volume 2, Chapter 6",
        "page": 169,
        "url": f"{REDBOOK_VOL2}#page=169",
        "summary": (
            "Language Environment provides a common runtime architecture for "
            "supported high-level language applications. Runtime initialization, "
            "enclaves, condition handling, storage management, callable services, "
            "and runtime options shape program behavior. Diagnose with the actual "
            "language, compiler/runtime level, messages, options, and application "
            "evidence; do not treat an LE option as a universal fix."
        ),
        "objectives": [
            "Describe LE as a shared runtime environment.",
            "Recognize enclaves, condition handling, and runtime options as concepts.",
            "Use LE messages and application context to guide diagnosis.",
        ],
        "practice": "A program reports an LE condition. What information should you gather before changing runtime options?",
        "answer": (
            "Capture the full message/condition token and traceback, job and step "
            "context, compiler/runtime levels, relevant LE options, input and "
            "reproduction conditions, and recent changes. Follow the program and "
            "installation's diagnostic procedures."
        ),
    },
    {
        "id": "address-spaces",
        "title": "Address spaces and virtual storage",
        "part": "Foundation · Related IBM Redbooks",
        "source": "ABCs of z/OS System Programming, Volumes 1 and 2",
        "page": 41,
        "url": f"{REDBOOK_VOL1}#page=41",
        "summary": (
            "An address space is a logical execution and virtual-addressing context, "
            "not a reserved slab of physical memory. z/OS maps private and common "
            "areas, and virtual storage is backed by real storage and paging "
            "resources as required. Access keys, address-space control, and "
            "cross-memory mechanisms are architectural details; use an approved "
            "reference before drawing operational conclusions."
        ),
        "objectives": [
            "Distinguish virtual storage from real storage.",
            "Describe private and common mappings conceptually.",
            "Relate an address space to jobs, system tasks, and isolation.",
        ],
        "practice": "A job's address space has a large virtual size. Does that directly mean the same quantity of central storage is occupied?",
        "answer": (
            "No. Virtual size and current real-storage backing are different "
            "measurements. Use system-specific displays and performance tools to "
            "understand actual residency and paging."
        ),
    },
    {
        "id": "dump-recovery",
        "title": "Diagnostic dumps, IPCS, backup, and restore",
        "part": "Foundation · Diagnosis and recovery",
        "source": "ABCs of z/OS System Programming, Volume 2, Chapter 1; see also Volume 8",
        "page": 23,
        "url": f"{REDBOOK_VOL2}#page=23",
        "summary": (
            "A diagnostic dump captures selected state for failure analysis; IPCS "
            "helps format and inspect supported dump data. A DFSMSdss backup dump "
            "is different: it is part of a data protection and recovery workflow "
            "that can include restore. A diagnostic dump is not a backup, and a "
            "backup is not proof that recovery works. Preserve evidence and test "
            "restores using an approved recovery plan."
        ),
        "objectives": [
            "Distinguish a diagnostic dump from a DFSMSdss backup dump.",
            "Describe IPCS as an analysis tool rather than a restore utility.",
            "Explain why restore testing and recovery plans matter.",
        ],
        "practice": "A system abends and a data set is also lost. Which separate workflows address diagnosis and recovery?",
        "answer": (
            "Preserve and analyze the diagnostic dump with IPCS alongside logs and "
            "messages to investigate the abend. Separately invoke the approved "
            "backup/recovery procedure to restore the lost data from a validated "
            "backup. Do not conflate these operations."
        ),
    },
]


COMMANDS = [
    ("TSO/E", "HELP", "Request command help, subject to installed help and authorization.", "volume1", 41, "IKJ56500I HELP INFORMATION (SIMULATED)\nUse site help for exact command syntax."),
    ("TSO/E", "TIME", "Display TSO/E session time information.", "volume1", 41, "READY\nTIME SHARING OPTION: TRAINING SESSION"),
    ("TSO/E", "LISTCAT LEVEL('USER1')", "List catalog entries under a naming level; output depends on the actual catalog.", "volume1", 41, "IDCAMS LISTCAT (SIMULATED)\nUSER1.LEARN.JCL       NONVSAM\nUSER1.LEARN.OUTPUT    NONVSAM\nCatalog not queried."),
    ("TSO/E", "LISTDS 'USER1.LEARN.JCL'", "Display information for a named data set when authorized.", "volume1", 41, "DATA SET LIST (SIMULATED)\nUSER1.LEARN.JCL\nNOT CONNECTED TO A CATALOG."),
    ("TSO/E", "SUBMIT 'USER1.LEARN.JCL'", "Submit a data set containing JCL to JES; simulator only checks pasted JCL.", "volume1", 41, "SUBMIT IS NOT CONNECTED TO JES.\nPaste sample JCL in the JCL editor and enter SUBMIT to run the structural checker."),
    ("TSO/E", "PROFILE", "Display or set attributes for the interactive TSO/E session.", "volume1", 41, "PROFILE (SIMULATED)\nPREFIX: STUDENT\nSession settings were not changed."),
    ("TSO/E", "STATUS", "Request status of the user's batch jobs where supported and authorized.", "volume1", 41, "STATUS (SIMULATED)\nTRAIN: OUTPUT (EXAMPLE)\nNo job was queried."),
    ("TSO/E", "ALLOCATE", "Allocate a DD name to a data set for the session; syntax and access are site-dependent.", "volume1", 41, "ALLOCATE (SIMULATED)\nNo DD name or data set was allocated."),
    ("TSO/E", "FREE", "Release a prior TSO/E allocation.", "volume1", 41, "FREE (SIMULATED)\nNo allocation was released."),
    ("TSO/E", "CANCEL", "Cancel an eligible job; this changes job state and requires correct authorization.", "volume1", 41, "SAFETY BLOCK\nCANCEL changes job state and is never issued by this simulator."),
    ("ISPF", "ISPF", "Start the ISPF dialog environment when configured.", "volume1", 41, "ISPF PRIMARY OPTION MENU (SIMULATED)\n1 VIEW   2 EDIT   3 UTILITIES\n4 FOREGROUND   5 BATCH   6 COMMAND\nX EXIT"),
    ("ISPF", "ISPF option 2 (EDIT)", "Select an ISPF panel option; this is a menu selection, not a TSO command.", "volume1", 41, "ISPF EDIT PANEL (SIMULATED)\nNo member or data set was opened."),
    ("SDSF", "SDSF", "Open the site-configured SDSF interface when installed and authorized.", "volume1", 41, "SDSF STATUS (SIMULATED)\nJOBNAME : TRAIN\nSTATUS  : OUTPUT\nNo JES job exists in this simulator."),
    ("SDSF", "ST", "Display the SDSF status panel (ST) when authorized.", "volume1", 41, "SDSF ST (SIMULATED)\nTRAIN JOB00001 OUTPUT\nNo JES job exists in this simulator."),
    ("SDSF", "DA", "Display active address spaces in SDSF when configured and authorized.", "volume1", 41, "SDSF DA (SIMULATED)\nTRAIN ASID 002A ACTIVE\nIllustrative only."),
    ("SDSF", "O", "Display output jobs in SDSF when configured and authorized.", "volume1", 41, "SDSF O (SIMULATED)\nTRAIN OUTPUT\nNo spool was queried."),
    ("SDSF", "H", "Display held output in SDSF when configured and authorized.", "volume1", 41, "SDSF H (SIMULATED)\nNo held output in this example."),
    ("MVS operator", "D A", "Display active address spaces; operator command, not a regular TSO command.", "volume2", 17, "IEE200I DISPLAY ACTIVITY (SIMULATED)\nJOBNAME : TRAIN\nASID    : 002A\nSTATUS  : ACTIVE"),
    ("MVS operator", "D IPLINFO", "Display information about the current IPL.", "volume2", 17, "DISPLAY IPLINFO (SIMULATED)\nIPL TYPE : CLPA (EXAMPLE)\nLOAD PARM: 0A82 (EXAMPLE)\nNo live system was queried."),
    ("MVS operator", "D PARMLIB", "Display information about active PARMLIB concatenations.", "volume2", 17, "DISPLAY PARMLIB (SIMULATED)\nSYS1.PARMLIB (EXAMPLE)\nNo live system was queried."),
    ("MVS operator", "D SSI", "Display subsystem-interface status information; exact output varies.", "volume2", 33, "DISPLAY SSI (SIMULATED)\nSUBSYSTEM: JES2\nSTATUS   : ACTIVE (EXAMPLE)"),
    ("MVS operator", "D PROG,LNKLST", "Display LNKLST set information; verify exact options for the installed release.", "volume2", 125, "DISPLAY PROG,LNKLST (SIMULATED)\nACTIVE SET: LNKLST00 (EXAMPLE)\nNo library was inspected."),
    ("MVS operator", "D PROG,APF", "Display APF list information; authorization changes require strict controls.", "volume2", 125, "DISPLAY PROG,APF (SIMULATED)\nAPF LIBRARY LIST (EXAMPLE)\nNo authorization state was queried."),
    ("MVS operator", "D SMF", "Request SMF status information; access/output depends on the release and system.", "volume2", 23, "DISPLAY SMF (SIMULATED)\nSMF STATUS: EXAMPLE ONLY"),
    ("MVS operator", "D GRS,C", "Display global resource serialization contention information; confirm operands for the installed release.", "volume2", 23, "DISPLAY GRS,C (SIMULATED)\nNO CONTENTION DATA WAS QUERIED."),
    ("MVS operator", "D WLM,SYSTEM", "Display workload-management system information; output is release/configuration dependent.", "volume2", 23, "DISPLAY WLM,SYSTEM (SIMULATED)\nNO WLM STATE WAS QUERIED."),
    ("MVS operator", "D LOGGER,LOGSTREAM", "Request system logger log-stream information; use the release-specific command reference.", "volume2", 23, "DISPLAY LOGGER (SIMULATED)\nNO LOG STREAM WAS QUERIED."),
    ("JES2 operator", "$D JOB", "Illustrative JES2 display command family. Not a TSO command.", "volume2", 51, "$HASP890 JOB (SIMULATED)\nJOBNAME=TRAIN  STATUS=OUTPUT\nNo JES2 command was issued."),
    ("JES2 operator", "$D SPOOL", "Illustrative JES2 spool display; exact supported operands are release/site-specific.", "volume2", 51, "$HASP646 SPOOL (SIMULATED)\nUTILIZATION: EXAMPLE ONLY\nNo spool was queried."),
    ("SMP/E", "SET BDY(GLOBAL).", "Select a CSI zone for following SMP/E commands.", "volume2", 159, "SMP/E COMMAND CONTEXT (SIMULATED)\nZONE: GLOBAL\nNo CSI was opened."),
    ("SMP/E", "SET BDY(TARGET).", "Select the intended target zone before applicable SMP/E operations.", "volume2", 159, "SMP/E COMMAND CONTEXT (SIMULATED)\nZONE: TARGET (EXAMPLE)\nNo CSI was opened."),
    ("SMP/E", "RECEIVE SYSMODS.", "Receive a valid SYSMOD package into SMP/E inventory.", "volume2", 159, "SMP/E RECEIVE (SIMULATED)\nNo package received."),
    ("SMP/E", "LIST SYSMOD(UM00001).", "List information about a SYSMOD known to the selected CSI.", "volume2", 159, "SMP/E LIST SYSMOD (SIMULATED)\nUM00001: EXAMPLE ONLY\nNo CSI was opened."),
    ("SMP/E", "APPLY CHECK SELECT(UM00001).", "Check applicability without applying the selected SYSMOD.", "volume2", 159, "SMP/E APPLY CHECK (SIMULATED)\nCHECK ONLY; NO CHANGE APPLIED.\nPrerequisites/HOLDDATA not evaluated."),
    ("SMP/E", "APPLY SELECT(UM00001).", "Apply a selected SYSMOD to a target zone; potentially changes system libraries.", "volume2", 159, "SAFETY BLOCK\nAPPLY changes system software and is not executed by this training application."),
    ("SMP/E", "ACCEPT SELECT(UM00001).", "Accept a SYSMOD into distribution libraries; requires controlled change procedures.", "volume2", 159, "SAFETY BLOCK\nACCEPT changes distribution libraries and is not executed by this training application."),
]


JCL_REFERENCE = [
    ("JOB", "//jobname JOB accounting,'description',CLASS=A,MSGCLASS=X", "Begins a job and supplies job-level identification and execution attributes."),
    ("EXEC", "//stepname EXEC PGM=program", "Begins a job step that invokes a program. EXEC can also invoke a cataloged procedure with PROC= or its name."),
    ("DD", "//ddname DD DSN=dataset,DISP=SHR", "Defines a data definition for a program step, such as a data set, SYSOUT destination, or in-stream data."),
    ("DD DUMMY", "//input DD DUMMY", "Defines an empty input data set or discards output, subject to program behavior."),
    ("DD *", "//SYSIN DD *", "Begins in-stream data in the job stream. Terminate the data with a delimiter line such as /*."),
    ("/*", "/*", "Ends in-stream data when used as a delimiter. Its meaning and placement depend on the JCL context."),
    ("//*", "//* explanatory comment", "JCL comment statement; it is not executed as a job step."),
    ("PROC", "//procname PROC", "Begins a cataloged or in-stream procedure definition; parameters and symbols may be supplied."),
    ("PEND", "// PEND", "Ends an in-stream procedure definition."),
    ("JCLLIB", "// MYLIB JCLLIB ORDER=(USER.PROCLIB)", "Specifies private libraries to search for procedures and INCLUDE groups."),
    ("INCLUDE", "// INCLUDE MEMBER=SETUP", "Includes a JCLLIB member into the JCL stream."),
    ("SET", "// SET ENV=TEST", "Assigns a symbolic parameter value for substitution in eligible JCL."),
    ("IF / THEN / ELSE / ENDIF", "// IF (STEP1.RC = 0) THEN", "Controls conditional execution of steps or in-stream procedures. This entry names the statement family; consult the IBM reference for complete syntax."),
    ("OUTPUT", "//OUT1 OUTPUT CLASS=A", "Defines output processing attributes referenced by applicable DD statements."),
    ("DD SYSOUT", "//REPORT DD SYSOUT=*", "Routes output to a JES output class; actual handling depends on JES and site configuration."),
    ("DD DISP", "//DATA DD DSN=USER.DATA,DISP=SHR", "Specifies data set disposition. Allocation and disposition syntax has additional operands and rules."),
    ("RESTART", "//TRAIN JOB ...,RESTART=STEP2", "Requests restart processing from a job step when supported and valid for the job; use approved restart procedures."),
]


INTERVIEW = [
    ("What does IPL mean?", "Initial program load: the controlled process that loads and initializes z/OS using selected system data sets and parameters."),
    ("What is SYS1.PARMLIB used for?", "It is the default/system parameter library location containing members used to configure system and subsystem behavior; installations may use concatenations and site-specific members."),
    ("What is the difference between a subsystem and SSI?", "A subsystem provides services. SSI is an interface mechanism through which eligible callers request services from registered subsystems."),
    ("What does JES do?", "JES manages batch job input, JCL processing, queues, execution handoff, and spool/output processing."),
    ("How do JES2 and JES3 differ?", "They are distinct job-entry subsystem products with different architectures, configuration, and command interfaces; use documentation for the installed subsystem."),
    ("Can a JES2 operator command be reused on JES3?", "Not without checking. JES3 has a distinct command interface and operational procedures; use the installed release's IBM reference and site runbook."),
    ("What should you inspect for a failed batch job?", "JESMSGLG, JESJCL, JESYSMSG, step SYSOUT/application logs, return codes, and correlated system messages."),
    ("What is LPA?", "The Link Pack Area is a set of system-managed virtual storage areas for modules made available for system-wide use; details depend on release/configuration."),
    ("What is LNKLST?", "A logical search order of libraries used to locate program modules under applicable loading rules."),
    ("Why is APF authorization sensitive?", "Authorized code can execute with elevated system privileges, so library ownership, content, access, and updates require strong controls."),
    ("What do LLA and VLF do?", "They support program-library directory management and virtual lookaside access/caching functions; they have different roles and configuration."),
    ("Name the main SMP/E zones.", "The global zone, target zones, and distribution zones, which record received maintenance and installed/distribution product inventories."),
    ("What is a SYSMOD?", "An SMP/E system modification package, such as a function, PTF, APAR, or USERMOD."),
    ("What does APPLY CHECK do?", "It checks whether selected maintenance can be applied and reports conditions without installing the change."),
    ("What does ACCEPT do?", "It accepts maintenance into distribution libraries; it is distinct from RECEIVE and APPLY and must follow change controls."),
    ("Why is a USERMOD not just a SYSMOD ID?", "A real USERMOD needs valid MCS and element content appropriate to an installed product, plus correct requisites and target libraries."),
    ("What is Language Environment?", "A common runtime architecture providing services such as initialization, condition handling, storage management, and callable services to supported language programs."),
    ("What is an address space?", "A logical execution and virtual-addressing context, not a fixed allocation of physical RAM."),
    ("How is a diagnostic dump different from a backup dump?", "A diagnostic dump captures state to analyze a failure. A DFSMSdss dump can be part of a backup/recovery workflow; IPCS analyzes diagnostic dumps."),
    ("Why is a non-zero return code not a full diagnosis?", "Its meaning depends on the program and step; logs, messages, application output, and business outcome must also be reviewed."),
    ("Which commands in this app are real?", "The examples demonstrate recognizable syntax, but every displayed result is generated locally and simulated; no command reaches z/OS."),
]


SCENARIO_STEPS = [
    {
        "task": "Inspect the simulated current IPL and parameter-library view.",
        "command": "D IPLINFO",
        "expected": "An illustrative IPL type and load parameter are displayed, marked as simulated.",
        "why": "A display is observational; it does not validate all initialization settings.",
    },
    {
        "task": "Review the sample active PARMLIB concatenation.",
        "command": "D PARMLIB",
        "expected": "A sample SYS1.PARMLIB entry appears.",
        "why": "PARMLIB contains configuration members; selected members/overrides vary by system.",
    },
    {
        "task": "Display the sample subsystem view.",
        "command": "D SSI",
        "expected": "A simulated JES2 entry appears.",
        "why": "Subsystem definition and availability must be checked with installed-system procedures.",
    },
    {
        "task": "Inspect a sample LNKLST view.",
        "command": "D PROG,LNKLST",
        "expected": "A simulated active set is shown.",
        "why": "Library search order affects module resolution and requires disciplined change control.",
    },
    {
        "task": "Paste the sample training JCL and run SUBMIT.",
        "command": "SUBMIT",
        "expected": "The structural checker reports job and step counts. It does not submit a job.",
        "why": "A real JES conversion is more comprehensive than this teaching validator.",
    },
    {
        "task": "Review the simulated JES2 display.",
        "command": "$D JOB",
        "expected": "An illustrative TRAIN job status appears.",
        "why": "JES2 operator commands are separate from TSO and actual state-changing commands are never executed here.",
    },
    {
        "task": "Set the SMP/E global-zone context in the simulator.",
        "command": "SET BDY(GLOBAL).",
        "expected": "A simulated GLOBAL zone context is displayed.",
        "why": "The simulator has no CSI; this only illustrates SMP/E command structure.",
    },
    {
        "task": "Run the safe dry-run example.",
        "command": "APPLY CHECK SELECT(UM00001).",
        "expected": "A simulated check-only message appears; no prerequisites are actually evaluated.",
        "why": "Only real SMP/E output from the target CSI can establish applicability.",
    },
]


LESSON_COMMANDS = {
    "tso-ispf-jcl-sdsf": ["HELP", "TIME", "LISTCAT LEVEL('USER1')", "LISTDS 'USER1.LEARN.JCL'", "ISPF", "SDSF"],
    "implementation": ["D IPLINFO", "D PARMLIB", "D SMF"],
    "parmlib-ipl": ["D IPLINFO", "D PARMLIB"],
    "catalog-smf-logs": ["LISTCAT LEVEL('USER1')", "D SMF"],
    "subsystems-ssi": ["D SSI"],
    "jes-job-flow": ["SUBMIT 'USER1.LEARN.JCL'", "SDSF"],
    "jes-commands": ["$D JOB", "$D SPOOL"],
    "lpa-lnklst-apf": ["D PROG,LNKLST", "D PROG,APF"],
    "smpe": [
        "SET BDY(GLOBAL).",
        "RECEIVE SYSMODS.",
        "APPLY CHECK SELECT(UM00001).",
        "APPLY SELECT(UM00001).",
        "ACCEPT SELECT(UM00001).",
    ],
    "language-environment": [],
    "address-spaces": ["D A"],
    "dump-recovery": ["D SMF"],
}


QUIZ = [
    {
        "question": "Which set contains the main z/OS installation control statements?",
        "options": ["PARMLIB members", "SDSF commands", "JES spool classes"],
        "answer": "PARMLIB members",
        "explanation": "PARMLIB members provide system and subsystem parameters selected during initialization and operation.",
    },
    {
        "question": "What does an IPL refer to?",
        "options": ["Initial program load and system initialization", "A JES output class", "A type of SMF record"],
        "answer": "Initial program load and system initialization",
        "explanation": "IPL is a controlled initialization sequence whose parameters and data sets must be verified.",
    },
    {
        "question": "Which statement about catalogs is correct?",
        "options": ["A catalog helps locate data sets", "A catalog is always the data set content", "A catalog replaces authorization checks"],
        "answer": "A catalog helps locate data sets",
        "explanation": "Catalog entries locate data sets; they are not the contents and do not replace security.",
    },
    {
        "question": "What is JES primarily responsible for?",
        "options": ["Batch input, job management, and output/spool", "Virtual storage translation", "Program compilation"],
        "answer": "Batch input, job management, and output/spool",
        "explanation": "JES receives, processes, queues, and manages batch job work and output.",
    },
    {
        "question": "Are JES2 and JES3 operator command syntaxes interchangeable?",
        "options": ["No, they are distinct subsystems", "Yes, all commands are identical", "Only during an IPL"],
        "answer": "No, they are distinct subsystems",
        "explanation": "Use the command reference for the installed JES product and site configuration.",
    },
    {
        "question": "What is the safe response to a JES2 command example on a JES3 system?",
        "options": ["Verify the JES3 command reference and local procedure", "Issue it unchanged", "Translate the dollar sign to an asterisk"],
        "answer": "Verify the JES3 command reference and local procedure",
        "explanation": "JES2 and JES3 interfaces and operational details are not interchangeable.",
    },
    {
        "question": "Why is APF authorization security-sensitive?",
        "options": ["It can permit code to run with elevated system privileges", "It compresses a PDS", "It changes a job class"],
        "answer": "It can permit code to run with elevated system privileges",
        "explanation": "Authorized libraries and their contents require strong access and change controls.",
    },
    {
        "question": "Which is the safest SMP/E command in this course's maintenance flow?",
        "options": ["APPLY CHECK", "ACCEPT", "APPLY"],
        "answer": "APPLY CHECK",
        "explanation": "APPLY CHECK checks and reports without installing; it is not a substitute for real CSI evaluation.",
    },
    {
        "question": "Which SMP/E zone tracks received SYSMODs?",
        "options": ["Global zone", "Only the target zone", "Only the distribution zone"],
        "answer": "Global zone",
        "explanation": "The global zone records received SYSMODs and related metadata.",
    },
    {
        "question": "What does ACCEPT do in SMP/E?",
        "options": ["Updates distribution libraries for accepted maintenance", "Runs a batch job", "Displays current address spaces"],
        "answer": "Updates distribution libraries for accepted maintenance",
        "explanation": "ACCEPT is separate from RECEIVE and APPLY and must follow change control.",
    },
    {
        "question": "What is Language Environment?",
        "options": ["A shared runtime architecture for supported programs", "A JES spool data set", "A PARMLIB member"],
        "answer": "A shared runtime architecture for supported programs",
        "explanation": "LE includes runtime initialization, condition handling, storage management, and callable services.",
    },
    {
        "question": "Does a larger virtual address-space size mean an equal amount of central storage is resident?",
        "options": ["No", "Yes, always", "Only for batch jobs"],
        "answer": "No",
        "explanation": "Virtual storage and current real-storage backing are different measurements.",
    },
    {
        "question": "What is the role of IPCS?",
        "options": ["Format and analyze supported dump data", "Apply maintenance", "Submit JCL"],
        "answer": "Format and analyze supported dump data",
        "explanation": "IPCS supports dump diagnosis; restoration is a separate recovery process.",
    },
    {
        "question": "Which is a TSO/ISPF distinction?",
        "options": ["TSO/E provides interactive command access; ISPF provides dialogs/panels", "ISPF is the batch scheduler", "TSO/E is the system logger"],
        "answer": "TSO/E provides interactive command access; ISPF provides dialogs/panels",
        "explanation": "They are related but distinct interactive environments.",
    },
    {
        "question": "What does the app's SUBMIT command do?",
        "options": ["Performs a basic local JCL structure check", "Submits to a real JES", "Writes to a real data set"],
        "answer": "Performs a basic local JCL structure check",
        "explanation": "No host is connected; the app never submits or runs the entered JCL.",
    },
    {
        "question": "A job has a non-zero return code. What is the best response?",
        "options": ["Review JES messages, step output, application logs, and code meaning", "Assume JES is broken", "Immediately purge the job"],
        "answer": "Review JES messages, step output, application logs, and code meaning",
        "explanation": "Return codes are evidence but are not a complete business or technical diagnosis.",
    },
]
