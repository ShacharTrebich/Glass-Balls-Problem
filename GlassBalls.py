import math

def checking_number(n: int, k: int) -> int:
    # אם יש רק קומה אחת או כדור אחד, מטפלים במקרים אלו ישירות
    if n == 0:
        return 0
    if n == 1:
        return 1
    if k == 1:
        return n

    # יצירת טבלה דו-ממדית בגודל (k+1) על (n+1)
    dp = [[0] * (n + 1) for _ in range(k + 1)]

    # מילוי מקרים בסיסיים
    for i in range(1, k + 1):
        dp[i][0] = 0  # אפס קומות דורש אפס בדיקות
        dp[i][1] = 1  # קומה אחת דורשת בדיקה אחת

    for j in range(1, n + 1):
        dp[1][j] = j  # כדור אחד דורש בדיקה של כל קומה אחת-אחת

    # מילוי הטבלה עבור יותר מכדור אחד ויותר מקומה אחת
    for i in range(2, k + 1):  # עבור כל מספר של כדורים
        for j in range(2, n + 1):  # עבור כל מספר של קומות
            dp[i][j] = float('inf')
            for x in range(1, j + 1):  # עבור כל קומה אפשרית
                # חישוב המקרה הגרוע ביותר
                res = 1 + max(dp[i - 1][x - 1], dp[i][j - x])
                dp[i][j] = min(dp[i][j], res)

    # מחזירים את התוצאה עבור k כדורים ו-n קומות
    return dp[k][n]

def index_floor(f_i: list[float], b: float) -> int:
    # אם הרשימה ריקה, נחזיר -1
    if not f_i:
        return -1

    # אם הכדור לא נשבר באף קומה
    if b >= f_i[-1]:
        return -1

    # חיפוש בינארי למציאת הקומה הראשונה שבה הכדור נשבר
    left, right = 0, len(f_i) - 1
    while left <= right:
        mid = (left + right) // 2
        if f_i[mid] > b:
            right = mid - 1
        else:
            left = mid + 1

    # מחזירים את הקומה (מספור החל מ-1)
    return left + 1

def index_first_floor(n: int) -> int:
    # חישוב ראשוני של x לפי הנוסחה הסגורה
    x = math.floor((-1 + math.sqrt(1 + 8 * n)) / 2)
    # אימות אם x מתאים או שיש לעלות ל-x+1
    if (x * (x + 1)) // 2 < n:
        return x + 1
    return x


