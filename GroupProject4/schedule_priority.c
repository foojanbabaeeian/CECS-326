/*
 * Priority scheduling
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

Task *pickNextTask() {
    struct node *temp = head;
    struct node *highestPriorityNode = temp;

    while (temp != NULL) {
        if (temp->task->priority > highestPriorityNode->task->priority) {
            highestPriorityNode = temp;
        }
        temp = temp->next;
    }
    return highestPriorityNode->task;
}

void schedule() {
    while (head != NULL) {
        Task *task = pickNextTask();
        run(task, task->burst); // Run the task for its entire burst time
        delete(&head, task); // Remove the task from the list after execution
    }
}