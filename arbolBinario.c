#include <stdio.h>
#include <stdlib.h>

// Estructura del nodo
typedef struct Node {
    int key;
    struct Node *left;
    struct Node *right;
} Node;

// Crear un nuevo nodo
Node* create_node(int key) {
    Node *n = malloc(sizeof(Node));
    if (!n) {
        perror("malloc");
        exit(EXIT_FAILURE);
    }
    n->key = key;
    n->left = n->right = NULL;
    return n;
}

// Insertar en el BST (recursivo)
Node* insert_node(Node *root, int key) {
    if (root == NULL) return create_node(key);

    if (key < root->key)
        root->left = insert_node(root->left, key);
    else if (key > root->key)
        root->right = insert_node(root->right, key);
    // si key == root->key no insertamos duplicados (podrías manejar duplicados según necesites)
    return root;
}

// Buscar un valor
Node* search(Node *root, int key) {
    if (root == NULL || root->key == key) return root;
    if (key < root->key) return search(root->left, key);
    return search(root->right, key);
}

// Encontrar el mínimo en un subárbol (usado para borrar)
Node* find_min(Node *root) {
    while (root && root->left) root = root->left;
    return root;
}

// Borrar un nodo por clave
Node* delete_node(Node *root, int key) {
    if (root == NULL) return NULL;

    if (key < root->key) {
        root->left = delete_node(root->left, key);
    } else if (key > root->key) {
        root->right = delete_node(root->right, key);
    } else {
        // Nodo encontrado
        if (root->left == NULL) {
            Node *tmp = root->right;
            free(root);
            return tmp;
        } else if (root->right == NULL) {
            Node *tmp = root->left;
            free(root);
            return tmp;
        } else {
            // Dos hijos: sustituir por el sucesor (mínimo del subárbol derecho)
            Node *succ = find_min(root->right);
            root->key = succ->key;
            root->right = delete_node(root->right, succ->key);
        }
    }
    return root;
}

// Recorridos
void inorder(Node *root) {
    if (!root) return;
    inorder(root->left);
    printf("%d ", root->key);
    inorder(root->right);
}

void preorder(Node *root) {
    if (!root) return;
    printf("%d ", root->key);
    preorder(root->left);
    preorder(root->right);
}

void postorder(Node *root) {
    if (!root) return;
    postorder(root->left);
    postorder(root->right);
    printf("%d ", root->key);
}

// Liberar todo el árbol
void free_tree(Node *root) {
    if (!root) return;
    free_tree(root->left);
    free_tree(root->right);
    free(root);
}

// Ejemplo de uso
int main(void) {
    Node *root = NULL;

    int valores[] = {50, 30, 20, 40, 70, 60, 80};
    int n = sizeof(valores) / sizeof(valores[0]);

    for (int i = 0; i < n; ++i)
        root = insert_node(root, valores[i]);

    printf("Recorridos del árbol:\n");
    printf("Inorden: ");
    inorder(root);
    printf("\nPreorden: ");
    preorder(root);
    printf("\nPostorden: ");
    postorder(root);
    printf("\n");

    // Buscar
    int clave = 40;
    Node *found = search(root, clave);
    printf("\nBusqueda de %d: %s\n", clave, found ? "ENCONTRADO" : "NO ENCONTRADO");

    // Borrar un nodo y mostrar inorden otra vez
    printf("\nBorramos 30...\n");
    root = delete_node(root, 30);
    printf("Inorden tras borrar 30: ");
    inorder(root);
    printf("\n");

    // Limpiar memoria
    free_tree(root);
    return 0;
}