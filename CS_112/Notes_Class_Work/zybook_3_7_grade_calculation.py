program_assignments1 = (float(input('Enter score of programming assignment 1 (score range 0-50) '))/50)
program_assignments2 = (float(input('Enter score of programming assignment 2 (score range 0-50) '))/50)
program_assignments3 = (float(input('Enter score of programming assignment 3 (score range 0-50) '))/50)
program_assignments4 = (float(input('Enter score of programming assignment 4 (score range 0-50) '))/50)
weighted_program_assignment = [program_assignments1, program_assignments2, program_assignments3, program_assignments4]
overall_program_assignment_score = sum(weighted_program_assignment) / 200

print(overall_program_assignment_score,)