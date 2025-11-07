# Multi-Class Study Time Planner
num_classes = int(input("Number of classes you're taking: "))
hours_available = float(input("Hours available to study per week: "))
exams_assignments = int(input("Exams/assignments coming up this week: "))
base_hours = hours_available / num_classes
priority_classes = int(input("Classes needing extra focus this week: "))
regular_classes = num_classes - priority_classes
bonus_hours = (hours_available * 0.2) / priority_classes if priority_classes > 0 else 0
priority_hours = base_hours + bonus_hours
regular_hours = base_hours - (bonus_hours * priority_classes / regular_classes) if regular_classes > 0 else 0
print(f"\n--- Study Plan ---")
print(f"Hours per regular class: {regular_hours:.1f} hours")
print(f"Hours per priority class: {priority_hours:.1f} hours")
print(f"Total study time: {hours_available:.1f} hours")
