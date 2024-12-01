/**
 * FCFS scheduling
 */

#include <stdlib.h>
#include <stdio.h>

#include "task.h"
#include "list.h"
#include "cpu.h"

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
    while (temp != NULL) {
        run(temp->task, temp->task->burst); // Run the task for its entire burst time
        temp = temp->next;
    }
}