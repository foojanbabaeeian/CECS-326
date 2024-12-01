/**
 * Round-robin scheduling
 */

#include <stdlib.h>
#include <stdio.h>

#include "task.h"
#include "list.h"
#include "cpu.h"

#define TIME_QUANTUM 10

// Define the head of the list of tasks
struct node *head = NULL;

void add(char *name, int priority, int burst) {
    Task *newTask = malloc(sizeof(Task));
    newTask->name = strdup(name);
    newTask->priority = priority;
    newTask->burst = burst;
    insert(&head, newTask);
}

void schedule() {
    struct node *temp = head;
    while (head != NULL) {
        if (temp->task->burst > TIME_QUANTUM) {
            run(temp->task, TIME_QUANTUM); // Run task for the time quantum
            temp->task->burst -= TIME_QUANTUM; // Decrease burst time
            temp = temp->next; // Move to next task
        } else {
            run(temp->task, temp->task->burst); // Run task for remaining burst time
            struct node *next = temp->next;
            delete(&head, temp->task); // Remove task from list
            temp = next; // Move to next task in the list
        }
        if (temp == NULL) temp = head; // Restart from head if end is reached
    }
}