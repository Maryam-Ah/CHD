def get_insight(question, options, insights):
    print("\n" + question)
    for idx, option in enumerate(options, 1):
        print(f"{idx}. {option}")
    
    while True:
        try:
            answer = int(input("\nEnter the number corresponding to your answer: "))
            if 1 <= answer <= len(options):
                return insights[answer - 1]
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Please enter a number corresponding to your answer.")

def main():
    insights_collected = []

    # Question 1
    question = "How often does your child use bright colors like red, yellow, or orange in their drawings?"
    options = ["Mostly", "Occasionally", "Rarely", "Never"]
    insights = [
        "Bright colors often signify high energy, enthusiasm, and happiness. Your child may have a vibrant and positive disposition.",
        "Your child occasionally uses bright colors, suggesting a balance in their emotional expression.",
        "Your child rarely using bright colors might indicate they lean towards more muted or nuanced expressions.",
        "A lack of bright colors might signify a preference for subtlety in their emotional expression."
    ]
    insights_collected.append(get_insight(question, options, insights))

    # Question 2
    question = "Does your child draw figures (like humans or animals) with faces and expressions?"
    options = ["Always", "Most of the time", "Sometimes", "Never"]
    insights = [
        "Drawing faces with distinct expressions can indicate your child's empathy and understanding of emotions.",
        "Mostly drawing faces suggests your child often reflects on emotions, either their own or of others.",
        "Drawing faces sometimes might hint at selective emotional expression.",
        "Not drawing faces could signify a preference for abstract representation or focus on non-emotional aspects."
    ]
    insights_collected.append(get_insight(question, options, insights))

    # Question 3
    question = "How does your child depict the sun in their drawings?"
    options = ["Big, bright, and central", "Small and in the corner", "Setting or rising", "Absent"]
    insights = [
        "A big, centrally-placed sun can indicate optimism and a cheerful disposition.",
        "A small sun in the corner suggests your child might be expressing happiness in a subdued manner.",
        "A setting sun might hint at transitions or endings in their perception.",
        "An absent sun might suggest feelings of gloom or a focus on other elements in their environment."
    ]
    insights_collected.append(get_insight(question, options, insights))

    # Question 4
    question = "When drawing a family, how close are the figures to each other?"
    options = ["Very close, almost touching", "Close but not touching", "Spread out with distance between them", "There's no consistent pattern"]
    insights = [
        "Very close figures indicate strong familial bonds and emotional closeness.",
        "Close figures suggest a sense of unity and togetherness in the family.",
        "Spread-out figures might suggest feelings of distance, independence, or varied relationships within the family.",
        "An inconsistent pattern indicates a dynamic representation and varied emotions towards family members."
    ]
    insights_collected.append(get_insight(question, options, insights))

    # Question 5
    question = "How often does your child incorporate natural elements like trees, flowers, or water in their drawings?"
    options = ["Always", "Often", "Rarely", "Never"]
    insights = [
        "Always incorporating natural elements indicates a strong connection with nature and their environment.",
        "Often using natural symbols might suggest a keen interest in the outdoors and growth.",
        "Rare use of nature hints at a focus on other elements or themes in their drawings.",
        "An absence of natural symbols doesn't diminish their connection to nature but might indicate a different focus in artistic expression."
    ]
    insights_collected.append(get_insight(question, options, insights))

    # Display Results
    print("\nBased on your answers, here are some general insights into your child's drawings:\n")
    for insight in insights_collected:
        print(f"- {insight}\n")

    print("Note: This quiz offers general interpretations and should not replace professional consultations. Every child is unique, and so is their art.")

if __name__ == "__main__":
    main()
