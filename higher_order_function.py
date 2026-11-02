# 1
# def apply_to_all(numbers, action):
#     result = []
#     for n in numbers:
#         result.append(action(n))
#     return result
#
# def double(n):
#     return n * 2
#
# def rounder(n):
#     return round(n)
#
# print(apply_to_all([1,2,3], double))
# print(apply_to_all([1.5, 5.6, 8.99], rounder))
# print(apply_to_all([1, 2, 3], lambda n: n * n))



# 2
# prices = [20, 75, 120, 45, 90]
# expensive_products = list(filter(lambda n: n> 50 , prices))
# print(expensive_products)
# print(list(map(lambda p: p + 10 , expensive_products)))



# 3
# words = ["banana" , "fig" , "cherry" , "kiwi"]
# students = [("Dana", 92), ("Avi", 78), ("Noa", 85)]
#
# print(sorted(words, key=len))
# print(max(words, key=len))
# print(list(map(lambda s: s[0] , sorted(students, key= lambda s: s[1], reverse= True))))



# 4
# לא הבנתי את השאלה



# 5
# הקריאה לפונקציה היא לא מונחת נכון
# היא אמורה לקרוא לפונקציית האב והיא אמורה לשלוח לבן את הפעולה
# הקריאה לא אמורה להיות משם
# התיקון הוא למחוק את הסוגריים אחרי הdouble ואז היא תעביר לאב את בוג הפעולה הנדרש והוא יעביר למקום הנכון


