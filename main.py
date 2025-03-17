import os
from openai import OpenAI

client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=os.environ["GITHUB_TOKEN"],
)


def choose_label(issue_content: str) -> str:
    """
    This function uses the OpenAI API to classify the issue content and suggest a label.
    """
    # Call the OpenAI API with the issue content
    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a repository manager for a GitHub repository. "
                "Your job is to assist users in managing their repositories, including creating issues, "
                "managing pull requests, and providing information about the repository.",
            },
            {
                "role": "user",
                "content": "Please decide which label to assign to the issue based on its content. "
                "Please produce only the label without any other texts. labels should be one of: enhancement,bug,question\n\n"
                f"<issue_content>\n{issue_content}\n</issue_content>\n\n",
            },
        ],
        model="gpt-4o",
        temperature=1,
        max_tokens=4096,
        top_p=1,
    )

    return response.choices[0].message.content.strip()


if __name__ == "__main__":
    # Choose a label for the issue
    label = choose_label("This does not work")
    print(label)
