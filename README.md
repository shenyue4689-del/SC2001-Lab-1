# SC2001-Lab-1 - Hybrid Merge Sort

This project implements and experimentally analyses a hybrid sorting algorithm that combines **Merge Sort** and **Insertion Sort**.

The hybrid algorithm uses Merge Sort for large subarrays and switches to Insertion Sort when the size of a subarray is less than or equal to a threshold value `S`.

---

## Project Structure

```text
SC2001-Lab-1-main/
│
├── src/
│   ├── part_a.py
│   ├── part_c_i_ii.py
│   └── part_c_iii.py
│
├── results/
│   └── part_c/
│       ├── console_outputs/
│       └── plots/
│
├── report/
│   └── SC2001_Part_C_Report.docx
│
├── README.md
└── .gitignore