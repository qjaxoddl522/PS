#include <stdio.h>
#include <string.h>

int main() {
    char word[1000000];
    int count = 0, len;
    
    scanf("%[^\n]s", word);
    len = strlen(word);
    
    if (len == 1 && word[0] == ' ') {
        printf("%d", count);
        
        return 0;
    }
    
    for (int i = 1; i < len - 1; i++) {
        if (word[i] == ' ') {
            count++;
        }
    }
    
    printf("%d", count + 1);
    
    return 0;
}