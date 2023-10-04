import streamlit as st

# Streamlit code for the "Drawing Analysis Quiz"
def get_insight(response, insights):
    return insights[response]

def main():
    st.title("Drawing Analysis Quiz: Decode the Artistic Expressions")
    st.write("""Every child's drawing is a masterpiece that holds clues to their inner world. Answer the following questions based on your child's drawings to uncover some intriguing insights. Remember, this quiz offers generalized interpretations and should be taken with a grain of fun!""")
    
    insights_collected = []

    # Questions and Insights
    questions = [
        "How often does your child use bright colors like red, yellow, or orange in their drawings?",
        "Does your child draw figures (like humans or animals) with faces and expressions?",
        "How does your child depict the sun in their drawings?",
        "When drawing a family, how close are the figures to each other?",
        "How often does your child incorporate natural elements like trees, flowers, or water in their drawings?"
    ]

    options_list = [
        ["Mostly", "Occasionally", "Rarely", "Never"],
        ["Always", "Most of the time", "Sometimes", "Never"],
        ["Big, bright, and central", "Small and in the corner", "Setting or rising", "Absent"],
        ["Very close, almost touching", "Close but not touching", "Spread out with distance between them", "There's no consistent pattern"],
        ["Always", "Often", "Rarely", "Never"]
    ]

    insights_list = [
        [
            "Bright colors often signify high energy, enthusiasm, and happiness. Your child may have a vibrant and positive disposition.",
            "Your child occasionally uses bright colors, suggesting a balance in their emotional expression.",
            "Your child rarely using bright colors might indicate they lean towards more muted or nuanced expressions.",
            "A lack of bright colors might signify a preference for subtlety in their emotional expression."
        ],
        [
            "Drawing faces with distinct expressions can indicate your child's empathy and understanding of emotions.",
            "Mostly drawing faces suggests your child often reflects on emotions, either their own or of others.",
            "Drawing faces sometimes might hint at selective emotional expression.",
            "Not drawing faces could signify a preference for abstract representation or focus on non-emotional aspects."
        ],
        [
            "A big, centrally-placed sun can indicate optimism and a cheerful disposition.",
            "A small sun in the corner suggests your child might be expressing happiness in a subdued manner.",
            "A setting sun might hint at transitions or endings in their perception.",
            "An absent sun might suggest feelings of gloom or a focus on other elements in their environment."
        ],
        [
            "Very close figures indicate strong familial bonds and emotional closeness.",
            "Close figures suggest a sense of unity and togetherness in the family.",
            "Spread-out figures might suggest feelings of distance, independence, or varied relationships within the family.",
            "An inconsistent pattern indicates a dynamic representation and varied emotions towards family members."
        ],
        [
            "Always incorporating natural elements indicates a strong connection with nature and their environment.",
            "Often using natural symbols might suggest a keen interest in the outdoors and growth.",
            "Rare use of nature hints at a focus on other elements or themes in their drawings.",
            "An absence of natural symbols doesn't diminish their connection to nature but might indicate a different focus in artistic expression."
        ]
    ]

    # Collect Responses
    for q, opts, ins in zip(questions, options_list, insights_list):
        response = st.selectbox(q, opts)
        insights_collected.append(get_insight(opts.index(response), ins))

    # Display Results
    if st.button("Get Insights"):
        st.header("Insights")
        for insight in insights_collected:
            st.write(insight)
        
        st.write("Note: This quiz offers general interpretations and should not replace professional consultations. Every child is unique, and so is their art.")

if __name__ == "__main__":
    main()
