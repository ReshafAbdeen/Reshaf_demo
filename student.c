#include <stdio.h>
#include <string.h>

struct Student {
    int roll_number;
    char name[50];
    float marks;
    char grade;
};

int main() {
    int n, found = 0;
    char search_name[50];

    printf("Enter number of students: ");
    scanf("%d", &n);

    struct Student students[n];

    for (int i = 0; i < n; i++) {
        printf("\nEnter details for student %d:\n", i + 1);
        
        printf("Roll Number: ");
        scanf("%d", &students[i].roll_number); 

        printf("Name: ");
        scanf("%s", students[i].name);         

        printf("Marks: ");
        scanf("%f", &students[i].marks);       

        printf("Grade: ");
        scanf(" %c", &students[i].grade);     
    }

    printf("\nEnter Student Name to search marks: ");
    scanf("%s", search_name);

    for (int i = 0; i < n; i++) {
        // strcmp se check karte hain ki naam match hua ya nahi
        if (strcmp(students[i].name, search_name) == 0) {
            printf("\nMarks of %s: %.2f\n Grade od %s: %c\n", students[i].grade, students[i].name, students[i].marks,  students[i].grade);
            printf("\nGrade od %s: %c\n", students[i].grade);
            found = 1; 
            break;     
    }
        }

    if (!found) {
        printf("\nStudent not found.\n");
    }

    return 0;
}