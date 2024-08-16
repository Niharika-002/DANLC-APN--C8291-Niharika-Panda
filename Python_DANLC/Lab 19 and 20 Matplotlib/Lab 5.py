
# Hi! Suppose I am a teacher, and I want to analyze the exam scores of my students
# to understand how they performed on a recent math test. I have collected the exam
# scores, and I want to create a histogram to visualize the distribution of scores. Can you
# please generate a complete code.
# [Note: You need to share the exam scores in list format. For eg.
# 22,45,60,75,80] sample data.

import matplotlib.pyplot as plt
exam_scores = [55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 60, 65, 70, 75, 80, 85, 90, 95, 100, 55]
bins = [50, 60, 70, 80, 90, 100, 110]

plt.figure(figsize=(10, 6))
plt.hist(exam_scores, bins=bins, edgecolor='black', color='y', alpha = 0.7)

plt.xlabel('Scores')
plt.ylabel('Number of Students')
plt.title('Distribution of Exam Scores')

# Display the plot
plt.show()