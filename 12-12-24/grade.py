def grade(project, internal, external):
    if project >= 50 and internal >= 50 and external >= 50:
        project = project * 0.70
        internal = internal * 0.10
        external = external * 0.20
        total_marks = project + internal + external
        if total_marks > 90:
            print("'A' grade")
        elif 80 < total_marks <= 90:
            print("'B' grade")
        else:
            print("'C' grade")
    else:
        if project < 50:
            print("Failed in project, score:", {project})
        if internal < 50:
            print("Failed in internal, score:", {internal})
        if external < 50:
            print("Failed in external, score:", {external})

project = int(input("Enter the marks in project:"))
internal = int(input("Enter the marks in internal:"))
external = int(input("Enter the marks in external:"))
grade(project, internal, external)
