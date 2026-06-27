# Excel Automation Instructions

## Input
- Source: Excel files in `data/` folder
- Each file may contain multiple tabs (Automotive, Tractors, Trucks & Buses – Vellore, Trucks & Buses – Red Hills, Infra, Parts)
- Supporting data comes from Balance Sheet (BS) and Trial Balance (TB) tabs for each division

## Output
- Consolidated Excel in `output/` folder
- Format must match `output_format.xlsx`
- Each division must have **Sources of Funds** and **Application of Funds** sections

---

## Transformation Rules

### Automotive
**Sources of Funds**
- Capital → Automotive BS
- P&L OP → Opening Balance from Automotive BS
- P&L C Y → Current Period from Automotive BS
- Loans → Automotive BS
- Supplier Creditors → Credit from sundry creditors (Automotive TB)
- Customer Advances → Credit from sundry debtors (Automotive TB)
- Other Liabilities → Current liabilities (Automotive BS) – sundry creditors (Automotive BS)
- Group Company → Branch/Divisions (Automotive BS)

**Application of Funds**
- Fixed Assets → Automotive BS
- Investment → Automotive BS
- Closing Stock → Automotive BS
- Sundry Debtors → Debit from sundry debtors (Automotive TB)
- Cash in Hand → Automotive BS
- Bank Accounts → Automotive BS
- Creditors Advance → Debit from sundry creditors (Automotive TB)
- Deposits & Advances → Current assets (Automotive BS) – [Closing Stock + Sundry Debtors + Cash in Hand + Bank Accounts + Deferred Tax]

---

### Tractors
(Same structure as Automotive, but values from Tractors BS/TB)

---

### TRR Trucks & Buses – Vellore
(Same structure, values from Vellore BS/TB)

---

### TRR Trucks & Buses – Red Hills
(Same structure, values from Red Hills BS/TB)

---

### Infra
(Same structure, values from Infra BS/TB)

---

### Parts
(Same structure, values from Parts BS/TB)

---

## Validation
- Totals must reconcile across divisions
- Log discrepancies in a separate file (`output/log.txt`)

## Output
- Save transformed data into `output/pl_structured.xlsx`
- Maintain formatting from `output_format.xlsx`
