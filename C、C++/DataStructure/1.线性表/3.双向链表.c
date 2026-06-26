#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>

typedef int E;

struct ListNode {
	E element;
	struct ListNode* prev;
	struct ListNode* next;
};
typedef struct ListNode LN;
typedef struct ListNode* Node;


void initList(Node node);		//链表的初始化
bool insertList(Node node, int index, E e);		// 按照位序插入元素
bool deleteList(Node node, int index);			// 删除元素
E* getList(Node node, int index);				// 查找1:按位查找，返回节点信息
int findList(Node node, E e);					// 查找2:按值查找，返回节点位置
int sizeList(Node node);		// 求链表的长度
void printList(Node node);		// 打印链表


void test01() {
	struct ListNode node;
	initList(&node);
	for (int i = 0;i < 6;i++) {
		insertList(&node, i + 1, i + 100);
	}
	printList(&node);

	printf("双向链表NodeList的长度为：%d\n", sizeList(&node));
	printf("%d ", *getList(&node, 3));
	printf("%d ", findList(&node, 201));
	printf("%d", findList(&node, 102));
}
void test02() {
	struct ListNode node;
	initList(&node);
	for (int i = 1;i <= 6;i++) {
		insertList(&node, i, i + 100);
	}
	deleteList(&node, 2);
	printList(&node);
}

int main() {
	test01();
	//test02();
	return 0;
}


void initList(Node node) {
	node->element = 0;
	node->next = NULL;
	node->prev = NULL;
}

bool insertList(Node node, int index, E e) {
	if (index < 1)return 0;

	while (--index) {
		if (node == NULL)return 0;

		node = node->next;
	}
	//Node newnode=(Node)malloc(sizeof(struct ListNode));
	Node newnode = (Node)malloc(sizeof(LN));
	if (newnode == NULL)return 0;

	newnode->element = e;

	if (node->next != NULL) {
		newnode->next = node->next;
		newnode->next->prev = newnode;
	}
	else {
		newnode->next = NULL;
	}

	newnode->prev = node;
	node->next = newnode;
	return 1;
}

bool deleteList(Node node, int index) {
	if (index < 1)return 0;
	while (index--) {
		node = node->next;
		if (node == NULL)return 0;
	}
	if (node->next == NULL) {
		node->prev->next = NULL;
	}
	else {
		node->prev->next = node->next;
		node->next->prev = node->prev;
	}
	free(node);
	return 1;
}
E* getList(Node node, int index) {
	while (index--) {
		if (node->next == NULL)return NULL;
		node = node->next;
	}
	return &node->element;
}
int findList(Node node, E e) {
	int cnt = 0;
	while (node!= NULL) {
		if (node->element == e)return cnt;

		node = node->next;
		cnt++;
	}
	return -1;
}
void printListf(Node node) {    // 遍历链表  
	while (node->next != NULL) {    // 正序遍历
		printf("%d", node->next->element);
		node = node->next;
		if (node->next!= NULL)printf("->");
	}puts("");

	while (node->prev != NULL) {    // 逆序遍历
		printf("%d", node->element);
		node = node->prev;
		if (node->prev != NULL)printf("->");
	}puts("");
}
int sizeList(Node node) {
	int cnt = 0;  
	while (node->next) {   
		node = node->next;
		cnt++;   
	}
	return cnt;
}