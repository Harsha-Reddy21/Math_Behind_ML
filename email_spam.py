def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a non-negative integer.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter an integer.")

total_emails = get_positive_int("Enter total number of emails: ")
emails_with_free = get_positive_int("Enter number of emails with the word 'free': ")
spam_emails = get_positive_int("Enter number of spam emails: ")
spam_and_free = get_positive_int("Enter number of emails that are both spam and contain 'free': ")


if (emails_with_free > total_emails or
    spam_emails > total_emails or
    spam_and_free > spam_emails or
    spam_and_free > emails_with_free):
    print("Inconsistent data. Please check your inputs.")
else:
    # Probabilities
    P_spam = spam_emails / total_emails
    P_free = emails_with_free / total_emails
    P_free_given_spam = spam_and_free / spam_emails

    # Bayes' Theorem
    P_spam_given_free = (P_free_given_spam * P_spam) / P_free

    # Output
    print(f"\nP(Spam | Free): {P_spam_given_free:.4f}")
