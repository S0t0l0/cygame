#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char* xor_decrypt(int* ciphertext, char* key, int ciphertext_len) {
    int key_len = strlen(key);
    char* decrypted = (char*)malloc(ciphertext_len + 1);
    int key_index = 0;

    for (int i = 0; i < ciphertext_len; i++) {
        char decrypted_char = ciphertext[i] ^ key[key_index];
        decrypted[i] = decrypted_char;

        key_index = (key_index + 1) % key_len;
    }

    decrypted[ciphertext_len] = '\0';

    return decrypted;
}

int main() {
    char* key2 = "nbgaLKSH";
    int flag[] = {34, 51, 38, 18, 6, 9, 26, 81, 3, 87, 57, 13, 82, 10, 3, 125, 37, 103, 127, 123, 99, 34, 27, 122, 125, 20, 123, 24, 97, 30, 120, 19, 117, 21, 116, 14};

    char username[100];
    printf("Username: ");
    scanf("%s", username);
    char* key1 = "AJAsklafkdf";

    printf("Enter your password, %s: ", username);
    char password[100];
    scanf("%s", password);

    char var1[] = "WOW Ignore ME";
    char* key3 = "JSLDKHKJGSAKL";

    if (strcmp(username, "DarkHelmet") == 0 && strcmp(password, "Not12345") == 0) {
        printf("Welcome back, Dark Helmet.\n");
        char yesorno[100];
        printf("Did you forget your secret code again? (yes/no) ");
        scanf("%s", yesorno);
        if (strcmp(yesorno, "yes") == 0) {
            char* concatenated_key = (char*)malloc(strlen(key1) + strlen(key2) + strlen(key3) + 1);
            strcpy(concatenated_key, key1);
            strcat(concatenated_key, key2);
            strcat(concatenated_key, key3);

            char* decrypted = xor_decrypt(flag, concatenated_key, sizeof(flag) / sizeof(flag[0]));
            printf("%s\n", decrypted);
            free(decrypted);
            free(concatenated_key);
        } else {
            printf("Yikes!\n");
        }
    } else {
        printf("Wait, you're obviously not Dark Helmet, I only take orders from Dark Helmet!... Go AWAY!\n");
    }

#if defined(_WIN32) || defined(_WIN64)
    system("pause"); // Windows: Pause the program
#else
    printf("Press Enter to exit...\n");
    getchar(); // Unix-based: Wait for Enter key press
#endif

    return 0;
}
