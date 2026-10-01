import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ============================================================
# STUDENT PERFORMANCE ANALYSIS - PBL 3
# ============================================================

FILE_NAME = "student_performance.csv"

# ------------------------------------------------------------
# Load Dataset
# ------------------------------------------------------------

try:
    df = pd.read_csv(FILE_NAME)

except FileNotFoundError:
    print("\nERROR: student_performance.csv not found!")
    print("Make sure the CSV file is in the same folder as this Python file.")
    input("\nPress Enter to exit...")
    exit()

original_rows = len(df)

# ------------------------------------------------------------
# Data Cleaning
# ------------------------------------------------------------

empty_rows_removed = df.isnull().all(axis=1).sum()

df = df.dropna(how="all")

duplicates_removed = df.duplicated().sum()

df = df.drop_duplicates()

# Fill remaining missing numerical values with median
numeric_columns = df.select_dtypes(include=np.number).columns

for column in numeric_columns:
    if df[column].isnull().sum() > 0:
        df[column] = df[column].fillna(df[column].median())

# Fill remaining missing categorical values with mode
categorical_columns = df.select_dtypes(exclude=np.number).columns

for column in categorical_columns:
    if df[column].isnull().sum() > 0:
        df[column] = df[column].fillna(df[column].mode()[0])

cleaned_rows = len(df)


# ============================================================
# 1. DISPLAY DATASET
# ============================================================

def display_dataset():

    print("\n" + "=" * 70)
    print("1. DATASET DISPLAY")
    print("=" * 70)

    print("\nFirst 10 Records:")
    print(df.head(10))

    print("\nLast 10 Records:")
    print(df.tail(10))

    print("\nDataset Shape:")
    print(df.shape)


# ============================================================
# 2. DATASET INFORMATION
# ============================================================

def dataset_information():

    print("\n" + "=" * 70)
    print("2. DATASET INFORMATION")
    print("=" * 70)

    print("\nNumber of Rows:", len(df))
    print("Number of Columns:", len(df.columns))

    print("\nColumn Names:")

    for i, column in enumerate(df.columns, start=1):
        print(f"{i}. {column}")

    print("\nData Types:")
    print(df.dtypes)

    print("\nDataset Information:")
    df.info()


# ============================================================
# 3. DATA CLEANING REPORT
# ============================================================

def cleaning_report():

    print("\n" + "=" * 70)
    print("3. DATA CLEANING REPORT")
    print("=" * 70)

    print("\nOriginal Records:", original_rows)

    print(
        "Completely Empty Rows Removed:",
        empty_rows_removed
    )

    print(
        "Duplicate Records Removed:",
        duplicates_removed
    )

    print(
        "Records After Cleaning:",
        cleaned_rows
    )

    print("\nMissing Values After Cleaning:")
    print(df.isnull().sum())

    print(
        "\nTotal Missing Values:",
        df.isnull().sum().sum()
    )


# ============================================================
# 4. DESCRIPTIVE STATISTICS
# ============================================================

def descriptive_statistics():

    print("\n" + "=" * 70)
    print("4. DESCRIPTIVE STATISTICS")
    print("=" * 70)

    print("\nStatistical Summary:")
    print(df.describe())

    print("\nMean:")
    print(
        df.select_dtypes(include=np.number).mean()
    )

    print("\nMedian:")
    print(
        df.select_dtypes(include=np.number).median()
    )

    print("\nStandard Deviation:")
    print(
        df.select_dtypes(include=np.number).std()
    )


# ============================================================
# 5. STUDY HOURS ANALYSIS
# ============================================================

def study_hours_analysis():

    print("\n" + "=" * 70)
    print("5. STUDY HOURS ANALYSIS")
    print("=" * 70)

    column = "StudyHours"

    if column not in df.columns:

        print("StudyHours column not found.")
        return

    data = df[column]

    print("\nStudy Hours Statistics:")

    print("Mean:", data.mean())
    print("Median:", data.median())
    print("Minimum:", data.min())
    print("Maximum:", data.max())
    print("Standard Deviation:", data.std())

    plt.figure(figsize=(8, 5))

    plt.hist(
        data,
        bins=10,
        edgecolor="black"
    )

    plt.title("Distribution of Study Hours")
    plt.xlabel("Study Hours")
    plt.ylabel("Number of Students")

    plt.tight_layout()
    plt.show()


# ============================================================
# 6. ATTENDANCE ANALYSIS
# ============================================================

def attendance_analysis():

    print("\n" + "=" * 70)
    print("6. ATTENDANCE ANALYSIS")
    print("=" * 70)

    column = "Attendance"

    if column not in df.columns:

        print("Attendance column not found.")
        return

    data = df[column]

    print("\nAttendance Statistics:")

    print("Mean:", data.mean())
    print("Median:", data.median())
    print("Minimum:", data.min())
    print("Maximum:", data.max())
    print("Standard Deviation:", data.std())

    plt.figure(figsize=(8, 5))

    plt.hist(
        data,
        bins=10,
        edgecolor="black"
    )

    plt.title("Attendance Distribution")
    plt.xlabel("Attendance")
    plt.ylabel("Number of Students")

    plt.tight_layout()
    plt.show()


# ============================================================
# 7. EXAM SCORE ANALYSIS
# ============================================================

def exam_score_analysis():

    print("\n" + "=" * 70)
    print("7. EXAM SCORE ANALYSIS")
    print("=" * 70)

    column = "ExamScore"

    if column not in df.columns:

        print("ExamScore column not found.")
        return

    data = df[column]

    print("\nExam Score Statistics:")

    print("Mean:", data.mean())
    print("Median:", data.median())
    print("Minimum:", data.min())
    print("Maximum:", data.max())

    print(
        "Range:",
        data.max() - data.min()
    )

    print(
        "Standard Deviation:",
        data.std()
    )

    print(
        "Variance:",
        data.var()
    )

    print("\nQuartiles:")

    print(
        "Q1:",
        data.quantile(0.25)
    )

    print(
        "Q2 / Median:",
        data.quantile(0.50)
    )

    print(
        "Q3:",
        data.quantile(0.75)
    )

    plt.figure(figsize=(8, 5))

    plt.hist(
        data,
        bins=10,
        edgecolor="black"
    )

    plt.title("Exam Score Distribution")
    plt.xlabel("Exam Score")
    plt.ylabel("Number of Students")

    plt.tight_layout()
    plt.show()


# ============================================================
# 8. PERFORMANCE DISTRIBUTION
# ============================================================

def performance_distribution():

    print("\n" + "=" * 70)
    print("8. PERFORMANCE DISTRIBUTION")
    print("=" * 70)

    if "ExamScore" not in df.columns:

        print("ExamScore column not found.")
        return

    def performance_category(score):

        if score >= 80:
            return "Excellent"

        elif score >= 60:
            return "Good"

        elif score >= 40:
            return "Average"

        else:
            return "Needs Improvement"

    performance = df[
        "ExamScore"
    ].apply(performance_category)

    counts = performance.value_counts()

    print("\nPerformance Categories:")
    print(counts)

    plt.figure(figsize=(8, 5))

    counts.plot(
        kind="bar",
        edgecolor="black"
    )

    plt.title("Student Performance Distribution")
    plt.xlabel("Performance Category")
    plt.ylabel("Number of Students")

    plt.xticks(rotation=0)

    plt.tight_layout()
    plt.show()


# ============================================================
# 9. GENDER-WISE ANALYSIS
# ============================================================

def gender_analysis():

    print("\n" + "=" * 70)
    print("9. GENDER-WISE ANALYSIS")
    print("=" * 70)

    if (
        "Gender" not in df.columns
        or
        "ExamScore" not in df.columns
    ):

        print("Required columns not found.")
        return

    result = df.groupby(
        "Gender"
    )["ExamScore"].agg(
        ["count", "mean", "min", "max"]
    )

    print("\nGender-wise Exam Score:")
    print(result)

    plt.figure(figsize=(8, 5))

    sns.barplot(
        data=df,
        x="Gender",
        y="ExamScore",
        errorbar=None
    )

    plt.title("Gender-wise Average Exam Score")
    plt.xlabel("Gender")
    plt.ylabel("Average Exam Score")

    plt.tight_layout()
    plt.show()


# ============================================================
# 10. ASSIGNMENT COMPLETION ANALYSIS
# ============================================================

def assignment_completion_analysis():

    print("\n" + "=" * 70)
    print("10. ASSIGNMENT COMPLETION ANALYSIS")
    print("=" * 70)

    if "AssignmentCompletion" not in df.columns:

        print("AssignmentCompletion column not found.")
        return

    data = df["AssignmentCompletion"]

    print("\nAssignment Completion Statistics:")

    print("Mean:", data.mean())
    print("Median:", data.median())
    print("Minimum:", data.min())
    print("Maximum:", data.max())
    print("Standard Deviation:", data.std())

    if "ExamScore" in df.columns:

        correlation = data.corr(
            df["ExamScore"]
        )

        print(
            "\nCorrelation with Exam Score:",
            correlation
        )

    plt.figure(figsize=(8, 5))

    plt.scatter(
        df["AssignmentCompletion"],
        df["ExamScore"],
        alpha=0.5
    )

    plt.title(
        "Assignment Completion vs Exam Score"
    )

    plt.xlabel("Assignment Completion")
    plt.ylabel("Exam Score")

    plt.tight_layout()
    plt.show()


# ============================================================
# 11. FINAL GRADE ANALYSIS
# ============================================================

def final_grade_analysis():

    print("\n" + "=" * 70)
    print("11. FINAL GRADE ANALYSIS")
    print("=" * 70)

    if "FinalGrade" not in df.columns:

        print("FinalGrade column not found.")
        return

    counts = (
        df["FinalGrade"]
        .value_counts()
        .sort_index()
    )

    print("\nFinal Grade Distribution:")
    print(counts)

    print("\nFinal Grade Percentages:")

    print(
        df["FinalGrade"]
        .value_counts(normalize=True)
        .sort_index()
        * 100
    )

    plt.figure(figsize=(8, 5))

    counts.plot(
        kind="bar",
        edgecolor="black"
    )

    plt.title("Final Grade Distribution")
    plt.xlabel("Final Grade")
    plt.ylabel("Number of Students")

    plt.tight_layout()
    plt.show()


# ============================================================
# 12. STRESS LEVEL ANALYSIS
# ============================================================

def stress_level_analysis():

    print("\n" + "=" * 70)
    print("12. STRESS LEVEL ANALYSIS")
    print("=" * 70)

    if "StressLevel" not in df.columns:

        print("StressLevel column not found.")
        return

    counts = (
        df["StressLevel"]
        .value_counts()
        .sort_index()
    )

    print("\nStress Level Distribution:")
    print(counts)

    if "ExamScore" in df.columns:

        print(
            "\nAverage Exam Score by Stress Level:"
        )

        result = (
            df.groupby("StressLevel")
            ["ExamScore"]
            .mean()
        )

        print(result)

    plt.figure(figsize=(8, 5))

    counts.plot(
        kind="bar",
        edgecolor="black"
    )

    plt.title("Stress Level Distribution")
    plt.xlabel("Stress Level")
    plt.ylabel("Number of Students")

    plt.tight_layout()
    plt.show()


# ============================================================
# 13. CORRELATION ANALYSIS
# ============================================================

def correlation_analysis():

    print("\n" + "=" * 70)
    print("13. CORRELATION ANALYSIS")
    print("=" * 70)

    numeric_df = df.select_dtypes(
        include=np.number
    )

    correlation = numeric_df.corr()

    print("\nCorrelation Matrix:")
    print(correlation)

    plt.figure(figsize=(12, 8))

    sns.heatmap(
        correlation,
        annot=True,
        cmap="coolwarm",
        fmt=".2f"
    )

    plt.title("Correlation Heatmap")

    plt.tight_layout()
    plt.show()


# ============================================================
# 14. RESOURCE ANALYSIS
# ============================================================

def resource_analysis():

    print("\n" + "=" * 70)
    print("14. RESOURCE ANALYSIS")
    print("=" * 70)

    if "Resources" not in df.columns:

        print("Resources column not found.")
        return

    if "ExamScore" in df.columns:

        result = (
            df.groupby("Resources")
            ["ExamScore"]
            .agg(
                ["count", "mean", "min", "max"]
            )
        )

        print("\nResources-wise Exam Score:")
        print(result)

    counts = (
        df["Resources"]
        .value_counts()
        .sort_index()
    )

    print("\nResource Distribution:")
    print(counts)

    plt.figure(figsize=(8, 5))

    counts.plot(
        kind="bar",
        edgecolor="black"
    )

    plt.title("Resource Distribution")
    plt.xlabel("Resources")
    plt.ylabel("Number of Students")

    plt.tight_layout()
    plt.show()


# ============================================================
# 15. INTERNET ACCESS ANALYSIS
# ============================================================

def internet_analysis():

    print("\n" + "=" * 70)
    print("15. INTERNET ACCESS ANALYSIS")
    print("=" * 70)

    if "Internet" not in df.columns:

        print("Internet column not found.")
        return

    counts = (
        df["Internet"]
        .value_counts()
        .sort_index()
    )

    print("\nInternet Access Distribution:")
    print(counts)

    if "ExamScore" in df.columns:

        result = (
            df.groupby("Internet")
            ["ExamScore"]
            .agg(
                ["count", "mean", "min", "max"]
            )
        )

        print("\nInternet-wise Exam Score:")
        print(result)

    plt.figure(figsize=(8, 5))

    counts.plot(
        kind="bar",
        edgecolor="black"
    )

    plt.title("Internet Access Distribution")
    plt.xlabel("Internet")
    plt.ylabel("Number of Students")

    plt.tight_layout()
    plt.show()


# ============================================================
# 16. KEY FINDINGS
# ============================================================

def key_findings():

    print("\n" + "=" * 70)
    print("16. KEY FINDINGS")
    print("=" * 70)

    print(
        "\nStudent Performance Analysis - Key Findings"
    )

    if "StudyHours" in df.columns:

        print(
            f"\n1. Average Study Hours: "
            f"{df['StudyHours'].mean():.2f}"
        )

    if "Attendance" in df.columns:

        print(
            f"2. Average Attendance: "
            f"{df['Attendance'].mean():.2f}"
        )

    if "ExamScore" in df.columns:

        print(
            f"3. Average Exam Score: "
            f"{df['ExamScore'].mean():.2f}"
        )

        print(
            f"4. Highest Exam Score: "
            f"{df['ExamScore'].max():.2f}"
        )

        print(
            f"5. Lowest Exam Score: "
            f"{df['ExamScore'].min():.2f}"
        )

    if "AssignmentCompletion" in df.columns:

        print(
            f"6. Average Assignment Completion: "
            f"{df['AssignmentCompletion'].mean():.2f}"
        )

    if (
        "ExamScore" in df.columns
        and
        "StudyHours" in df.columns
    ):

        study_corr = df[
            "StudyHours"
        ].corr(
            df["ExamScore"]
        )

        print(
            f"7. Study Hours vs Exam Score Correlation: "
            f"{study_corr:.3f}"
        )

    if (
        "ExamScore" in df.columns
        and
        "Attendance" in df.columns
    ):

        attendance_corr = df[
            "Attendance"
        ].corr(
            df["ExamScore"]
        )

        print(
            f"8. Attendance vs Exam Score Correlation: "
            f"{attendance_corr:.3f}"
        )

    if (
        "ExamScore" in df.columns
        and
        "AssignmentCompletion" in df.columns
    ):

        assignment_corr = df[
            "AssignmentCompletion"
        ].corr(
            df["ExamScore"]
        )

        print(
            f"9. Assignment Completion vs Exam Score Correlation: "
            f"{assignment_corr:.3f}"
        )

    print(
        "\n10. Dataset contains "
        f"{len(df)} cleaned student records."
    )

    print(
        "\nNOTE: Numeric category codes such as Gender, "
        "Resources, Internet, StressLevel and FinalGrade "
        "are displayed according to the dataset values. "
        "Their exact meanings should be taken from the "
        "dataset/data dictionary."
    )


# ============================================================
# MAIN MENU
# ============================================================

def main():

    while True:

        print("\n")
        print("=" * 70)
        print("       STUDENT PERFORMANCE ANALYSIS")
        print("=" * 70)

        print("\n1.  Display Dataset")
        print("2.  Dataset Information")
        print("3.  Data Cleaning Report")
        print("4.  Descriptive Statistics")
        print("5.  Study Hours Analysis")
        print("6.  Attendance Analysis")
        print("7.  Exam Score Analysis")
        print("8.  Performance Distribution")
        print("9.  Gender-wise Analysis")
        print("10. Assignment Completion Analysis")
        print("11. Final Grade Analysis")
        print("12. Stress Level Analysis")
        print("13. Correlation Analysis")
        print("14. Resource Analysis")
        print("15. Internet Access Analysis")
        print("16. Key Findings")
        print("17. Exit")

        print("\n" + "-" * 70)

        choice = input("Enter your choice (1-17): ")

        if choice == "1":
            display_dataset()

        elif choice == "2":
            dataset_information()

        elif choice == "3":
            cleaning_report()

        elif choice == "4":
            descriptive_statistics()

        elif choice == "5":
            study_hours_analysis()

        elif choice == "6":
            attendance_analysis()

        elif choice == "7":
            exam_score_analysis()

        elif choice == "8":
            performance_distribution()

        elif choice == "9":
            gender_analysis()

        elif choice == "10":
            assignment_completion_analysis()

        elif choice == "11":
            final_grade_analysis()

        elif choice == "12":
            stress_level_analysis()

        elif choice == "13":
            correlation_analysis()

        elif choice == "14":
            resource_analysis()

        elif choice == "15":
            internet_analysis()

        elif choice == "16":
            key_findings()

        elif choice == "17":

            print(
                "\nThank you for using "
                "Student Performance Analysis!"
            )

            break

        else:

            print(
                "\nInvalid choice! "
                "Please enter a number from 1 to 17."
            )




# ============================================================
# PROGRAM START
# ============================================================

if __name__ == "__main__":
    main()