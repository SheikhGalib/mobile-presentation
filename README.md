# Presentation: Designing for a Unified Experience
## Paper: "Designing for a Unified Experience: A New Perspective and a Case Study"
### Authors: Wei Xu, Dov Furie — Intel Corporation

---

## 📋 WHAT YOU NEED TO KNOW (TL;DR for the group)

**Paper in one line:** Enterprise software is a UX nightmare because employees use dozens of broken, siloed apps — this paper proposes a "Unified Experience" framework (5 attributes + implementation strategy) and proves it works via a real Intel supply chain case study.

**Key takeaway:** By redesigning business processes, integrating systems, and optimizing touchpoints, they cut task time from 10 min → 5 min, reduced apps from 6 → 1, clicks from 69 → 17, and saved $1.2M per buyer.

---

## 🎯 SLIDE FLOW (5-minute presentation, ~10-12 slides)

### Slide 1: Title Slide
- **Title:** Designing for a Unified Experience: A New Perspective and a Case Study
- **Course:** [Course No. & Name]
- **Teacher:** [Teacher Name]
- **KUET Logo** (top-right or center)
- **Group Members:** [Names & Rolls]
- **Date:** February 2026

---

### Slide 2: Table of Contents / Roadmap
Quick visual roadmap:
1. The Problem — Why Enterprise UX is Broken
2. What Others Tried (& Why It Wasn't Enough)
3. The Solution — Unified Experience Framework
4. Case Study — Meet Paul, the Frustrated Buyer
5. Results — Hard Numbers That Prove It Works
6. Takeaways & Exam-Ready Points

---

### Slide 3: The Problem — Broken Enterprise UX 🔥
**Hook question:** "Imagine using 6+ different apps just to do ONE task at work... every single day."

Key points:
- Large companies = hundreds of apps (CRM, SCM, ERP, HR, BI...)
- Apps come from mergers, acquisitions, different vendors, home-grown tools
- Result: **Hybrid, siloed environment**
  - Inconsistent UIs
  - Fragmented business processes
  - Poor data integration
  - Broken workflows across apps
- **Impact on users:**
  - Low productivity
  - Frustration & high support call volume
  - Poor decision-making
  - Increased errors and rework

**Visual:** Diagram showing multiple disconnected apps with a confused user in the middle

---

### Slide 4: Previous Approaches — What Others Tried
| Approach | Who | What They Did | Limitation |
|----------|-----|---------------|------------|
| Uniform Visual Design | Google (Material Design), Cooper | Consistent look & feel across apps | Only surface-level — doesn't fix broken workflows |
| Unified Customer Experience | Rogowski/Forrester | Seamless cross-channel touchpoints | Limited to digital marketing domain |
| Unified Architecture | O'Toole | Integrated backend/database | No front-end or process design details |
| Vendor Partnership | Finstad, Xu et al. | Bridge gap between vendors & users | Doesn't address full end-to-end UX |
| Klocek's Hierarchy Model | Klocek (Smashing Mag) | 5-level pyramid: visual → organizational shift | Too linear, visual design overemphasized, business process redesign placed too late |

**Key criticism of Klocek's model:**
- Overemphasizes visual design as foundation
- Doesn't fit hybrid vendor environments (can't easily customize vendor apps)
- Business process redesign comes too late
- Linear model doesn't match reality

---

### Slide 5: The Solution — Unified Experience Definition (5 Attributes) ⭐
**This is the CORE of the paper**

```
┌─────────────────────────────────────┐
│       UNIFIED EXPERIENCE            │
│                                     │
│  1. Consistency                     │
│     → Uniform visual/branding       │
│                                     │
│  2. Efficiency                      │
│     → Streamlined business          │
│       processes                     │
│                                     │
│  3. Personalization                 │
│     → Right content, right device,  │
│       right context                 │
│                                     │
│  4. Integration                     │
│     → Data, security, architecture  │
│       across apps                   │
│                                     │
│  5. Optimization                    │
│     → Seamless end-to-end           │
│       touchpoints (performance,     │
│       usability, help, support)     │
└─────────────────────────────────────┘
```

**Remember (exam): Norman & Nielsen's UX definition** — "UX encompasses ALL aspects of the end-user's interaction with the company, its services, and its products." Unified Experience extends this to MULTIPLE applications in a business context.

---

### Slide 6: Implementation Framework (2 Driving Vectors)
**Two approaches that work together:**

```
         TOP-DOWN (Organization)
    ┌──────────────────────────────┐
    │  UX Culture                  │
    │  Organizational Commitment   │
    ├──────────────────────────────┤
    │  UX Standards                │
    │  UI Assets                   │
    │  Integration Framework       │
    │  UX Practices                │
    │  Vendor Strategy             │
    │  Governance                  │
    └──────────────────────────────┘
         BOTTOM-UP (Design)
```

**Key features of this framework vs. others:**
- ✅ End-to-end systematic view
- ✅ Holistic (all user touchpoints)
- ✅ Realistic & specific (works with vendor solutions)
- ✅ Adaptive & opportunistic (start anywhere)
- ✅ UX metric-driven (prove ROI)
- ✅ Tactical (specific tools & approaches)

---

### Slide 7: Case Study — Meet Paul 👤
**Story-driven slide (make it relatable)**

- **Paul** = buyer at a global company's supply chain
- Works with factory spare parts inventory
- **His daily nightmare:**
  - Uses **6+ different apps** to do his job
  - **35 manual steps** per task
  - **69 mouse clicks** per transaction
  - Copies/pastes data between screens
  - Sends dozens of manual emails
  - Makes mistakes due to complexity
  - **10 minutes per task** average
  - Lives in constant firefighting mode

**Three core problems:**
| Problem | Impact | Severity |
|---------|--------|----------|
| Long Cycle Time | Low productivity, late orders | HIGH |
| Incorrect Priorities | Factory escalations | HIGH |
| Quality Issues | Rework, cost | HIGH |

---

### Slide 8: Design Principles (How They Fixed It)
**6 Design Principles for the new system (BOMA):**

| # | Principle | What It Means |
|---|-----------|---------------|
| 1 | Standardize the process | Single version of process |
| 2 | Integrate Business Intelligence | Minimum info for decision-making on ONE screen |
| 3 | Reduce siloed systems | Integrate data from multiple sources |
| 4 | Collaborate online | Replace email with digital collaboration |
| 5 | Eliminate rework | Verify data at point of entry |
| 6 | Self-service for customers | Dashboard for stakeholders |

**Technology:** Business Process Management Suite (BPMS) + Service Oriented Architecture (SOA)

---

### Slide 9: Results — The Numbers 📊 (Most Important Slide!)
**Before vs. After Comparison:**

| Category | Metric | BEFORE | AFTER |
|----------|--------|--------|-------|
| **Process** | Manual Steps | 35 | **12** |
| | Manual Processes | 7 | **1** |
| | Roles | 5 | **4** |
| | Rework Rate | 20% | **<5%** |
| **Integration** | Applications | 6 | **1** |
| | Screens | 15 | **3** |
| | Automated Steps | 8 | **23** |
| **Optimization** | Manual Emails | Dozens | **None** |
| | Help | Partial | **Comprehensive** |

**Business Value (3 months after deployment):**

| Metric | Before | After |
|--------|--------|-------|
| Avg task time | 10 min | **5 min** |
| Clicks per transaction | 69 | **17** |
| Late orders | 40% | **20%** |
| Cost savings per buyer | $0 | **$1.2 Million** |
| Training time | Dozens of hours | **2 hours** |
| "How do I" tickets | Dozens | **0** |
| User agrees with system recommendation | <10% | **83%** |
| User feeling | Frustrated | **Enthusiastic** |

---

### Slide 10: Key Takeaways & Lessons Learned
1. **UX is NOT just about UI** — It's about the entire end-to-end experience
2. **Business process redesign** is crucial — prettier UI alone won't help
3. **Integration** across apps eliminates context-switching pain
4. **Metric-driven approach** is key — measure productivity, cost, satisfaction
5. **Phased implementation** — start where you can, expand systematically
6. **UX professionals must partner** with business + tech teams
7. **Fewer vendor platforms = better unified experience** long-term

---

### Slide 11: Exam-Ready Quick Reference 📝
**Definition:** Unified Experience = Consistency + Efficiency + Personalization + Integration + Optimization

**Framework has 2 Driving Vectors:**
1. Organization (top-down): UX Culture + Organizational Commitment
2. Design (bottom-up): UX Standards, UI Assets, Integration Framework, UX Practices, Vendor Strategy, Governance

**Klocek's 5-Level Pyramid (what they improved upon):**
1. Consistent Visual Design
2. Consistent Interaction Behavior
3. Rework Products for User Needs
4. Design Unified Experience
5. Transform Organization

**Case Study Key Numbers to Remember:**
- 35 → 12 manual steps
- 6 → 1 applications
- 69 → 17 clicks
- 10 min → 5 min task time
- $1.2M saved per buyer
- 2 hours training (from dozens)

**Norman & Nielsen UX Definition:** "UX encompasses all aspects of the end-user's interaction with the company, its services, and its products."

---

### Slide 12: Thank You / Q&A
- Group member names
- "Any questions?"
- Reference: Xu, W. & Furie, D. — "Designing for a Unified Experience" (Intel Corporation)

---

## 🎙️ SPEAKER SCRIPT (5 minutes)

### [0:00 - 0:30] Opening (Slide 1-2)
"Good morning everyone. Today we're presenting a paper about Unified Experience Design. Let's jump in — here's what we'll cover."

### [0:30 - 1:15] The Problem (Slide 3)
"Imagine you need to use SIX different apps just to complete ONE task at work. That's what enterprise employees face daily. Large companies end up with hundreds of apps — from different vendors, built at different times, with different UIs. The result? Broken, fragmented experience. Users waste time switching between apps, copying data manually, and making errors. This paper tackles exactly this problem."

### [1:15 - 1:45] What Others Tried (Slide 4)
"People have tried to fix this before. Google's Material Design made apps look consistent. Others tried unifying the backend architecture. Klocek proposed a 5-level pyramid — but his model overemphasizes visual design and puts business process redesign too late. None of these approaches were comprehensive enough."

### [1:45 - 2:30] The Solution (Slides 5-6)
"So the authors propose a comprehensive Unified Experience framework with 5 key attributes: Consistency, Efficiency, Personalization, Integration, and Optimization. And they provide an implementation framework with two driving vectors — Organization from the top-down, and Design from the bottom-up. The beauty is you can start from anywhere based on your company's maturity level."

### [2:30 - 3:30] Case Study — Paul (Slides 7-8)
"Let's make this real. Meet Paul — a buyer at Intel's supply chain. He used 6 apps, 35 manual steps, 69 clicks per transaction. Total nightmare. They redesigned his workflow using 6 design principles — standardize the process, integrate BI, reduce silos, enable online collaboration, eliminate rework, and enable self-service. They used a Business Process Management Suite to build a new unified app called BOMA."

### [3:30 - 4:30] Results (Slide 9)
"And here's the payoff — this is the most important slide. Manual steps dropped from 35 to 12. Applications from 6 to 1. Clicks from 69 to 17. Task time was cut in half. And each buyer saved $1.2 million. Training dropped from dozens of hours to just 2 hours. Most impressively, users went from frustrated to enthusiastic."

### [4:30 - 5:00] Closing (Slides 10-12)
"Key takeaway: UX is not just about making things look pretty. It's about redesigning the entire experience — processes, integration, and all touchpoints. Thank you! Any questions?"

---

## 📌 IMPORTANT EXAM POINTS SUMMARY

1. **What is Unified Experience?** A comprehensive approach to delivering end-to-end experience across multiple applications with 5 attributes: Consistency, Efficiency, Personalization, Integration, Optimization.

2. **What is the problem in enterprise software?** Hybrid environment of vendor solutions + home-grown apps = siloed, inconsistent, broken UX.

3. **Why is Klocek's model insufficient?** Overemphasizes visual design, too linear, doesn't address vendor constraints, places business process redesign too late.

4. **What are the 2 Driving Vectors of the implementation framework?** Organization (top-down: UX culture, commitment) and Design (bottom-up: standards, assets, practices, governance).

5. **What are the 6 Design Principles from the case study?** Standardize process, Integrate BI, Reduce silos, Collaborate online, Eliminate rework, Self-service.

6. **What technology enabled the case study solution?** BPMS (Business Process Management Suite) + SOA (Service Oriented Architecture).

7. **What were the key improvements?** 35→12 steps, 6→1 apps, 69→17 clicks, 10→5 min task time, $0→$1.2M savings, 20%→<5% rework.
