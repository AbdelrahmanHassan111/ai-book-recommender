import gradio as gr
import pandas as pd
import joblib
import warnings
import os
warnings.filterwarnings('ignore')

# File loading function
def load_files():
    try:
        tfidf = joblib.load('tfidf_model.pkl')
        book_cosine_sim = joblib.load('cosine_similarity_matrix.pkl')
        books_df = pd.read_csv('book_names.csv')
        
        books = books_df.iloc[:, 0] if len(books_df.columns) == 1 else books_df.iloc[:, 0]
        return tfidf, book_cosine_sim, books
    except Exception as e:
        print(f"Error loading files: {str(e)}")
        return None, None, None

# Recommendation function
def recommend_books_similar_to(book_name, n=5, cosine_sim_mat=None):
    try:
        book_name = book_name.strip()
        matching_books = books[books.str.lower() == book_name.lower()]
        
        if matching_books.empty:
            return ["Book not found. Please check the spelling and try again."]
        
        input_idx = matching_books.index[0]
        sim_scores = pd.Series(cosine_sim_mat[input_idx])
        top_n_books_idx = sim_scores.sort_values(ascending=False).iloc[1:n+1].index
        
        return [f"{i+1}. {books[idx]}" for i, idx in enumerate(top_n_books_idx)]
    except Exception as e:
        return [f"An error occurred: {str(e)}"]

# Interface function
def book_recommender_interface(book_name, num_recommendations):
    if not book_name:
        return "Please enter a book name."
    return "\n".join(recommend_books_similar_to(book_name, num_recommendations, book_cosine_sim))

# Load models and data
tfidf, book_cosine_sim, books = load_files()
# CSS Styling
css = """
.gradio-container {
    font-family: 'Poppins', sans-serif;
    background: linear-gradient(to bottom right, #ffffff, #f5f7fa);
}
.gr-button {
    background: linear-gradient(to right, #4776E6, #8E54E9);
    border: none;
    color: white;
    font-size: 16px;
    border-radius: 12px;
    transition: all 0.3s ease;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
}
.gr-button:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(0,0,0,0.15);
    background: linear-gradient(to right, #3867D6, #7B42D6);
}
.gr-input, .gr-box {
    border-radius: 12px;
    border: 2px solid #e6e8eb;
    transition: all 0.3s ease;
}
.gr-input:focus {
    border-color: #4776E6;
    box-shadow: 0 0 0 2px rgba(71, 118, 230, 0.2);
}
.feature-card {
    background: white;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    transition: transform 0.3s ease;
}
.feature-card:hover {
    transform: translateY(-5px);
}
.example-text {
    color: #000000 !important;
}
.example-header {
    color: #000000 !important;
}
.custom-examples-box {
    background: white;
    padding: 15px;
    border-radius: 12px;
    margin-top: 10px;
}
.custom-examples-box * {
    color: #000000 !important;
}
"""

# Gradio Interface
with gr.Blocks(css=css, theme=gr.themes.Soft()) as demo:
    # Header
    gr.Markdown(
        """
        <div style="text-align: center; padding: 20px; background: linear-gradient(120deg, #4776E6, #8E54E9); border-radius: 16px; margin-bottom: 24px;">
            <h1 style="font-size: 3em; margin-bottom: 10px; color: white;">📚 AI Book Recommender</h1>
            <p style="font-size: 1.2em; color: black;">Discover your next favorite book using AI-powered recommendations</p>
        </div>
        """
    )

    # Features
    gr.Markdown(
        """
        <div style="display: flex; gap: 20px; margin: 20px 0;">
            <div class="feature-card">
                <h3 style="color: #000000;">🎯 Precise Matching</h3>
                <p style="color: #000000;">Our AI analyzes thousands of books to find perfect matches</p>
            </div>
            <div class="feature-card">
                <h3 style="color: #000000;">🔍 Smart Search</h3>
                <p style="color: #000000;">Case-insensitive search with intelligent error handling</p>
            </div>
            <div class="feature-card">
                <h3 style="color: #000000;">⚡ Fast Results</h3>
                <p style="color: #000000;">Get instant recommendations in seconds</p>
            </div>
        </div>
        """
    )

    # Main Interface
    with gr.Row():
        with gr.Column():
            book_name = gr.Textbox(
                label="📖 Enter Book Title",
                placeholder="e.g., 'The Great Gatsby'",
                lines=2
            )
            num_recommendations = gr.Slider(
                minimum=1,
                maximum=10,
                value=5,
                step=1,
                label="🎯 Number of Recommendations"
            )
            recommend_button = gr.Button("✨ Get Recommendations", variant="primary")
        
        with gr.Column():
            output = gr.Textbox(
                label="📚 Recommended Books",
                lines=12,
                interactive=False
            )
    gr.Markdown(
        """
        <div style="margin-top: 24px; padding: 20px; background: white; border-radius: 12px;">
            <h3 style="color: #000000; margin-bottom: 15px;">🔠 Exambles</h3>
            <ol>
                <li style="color: #000000;">data structures & other objects using java</li>
                <li style="color: #000000;">the big island</li>
                <li style="color: #000000;">how to build outdoor structures</li>
                <li style="color: #000000;">chicago's southeast side (images of america: illinois)</li>
            </ol>
        </div>
        """
    )

    
    # How it Works
    gr.Markdown(
        """
        <div style="margin-top: 24px; padding: 20px; background: white; border-radius: 12px;">
            <h3 style="color: #000000; margin-bottom: 15px;">🤔 How It Works</h3>
            <ol>
                <li style="color: #000000;">Enter the title of a book you enjoyed</li>
                <li style="color: #000000;">Or copy example from the provided examples</li>
                <li style="color: #000000;">Choose how many recommendations you want (1-10)</li>
                <li style="color: #000000;">Click the "Get Recommendations" button</li>
                <li style="color: #000000;">Discover new books tailored to your taste!</li>
            </ol>
        </div>
        """
    )

    # Footer
    gr.Markdown(
        """
        <div style="text-align: center; margin-top: 30px;">
            <p style="color: #000000;">Made with ❤️ for book lovers | Version 2.1</p>
            <p style="color: #000000; font-size: 0.8em;">Powered by AI and curated with care</p>
        </div>
        """
    )

    # Set up click event
    recommend_button.click(
        book_recommender_interface,
        inputs=[book_name, num_recommendations],
        outputs=output
    )

if __name__ == "__main__":
    if tfidf is None or book_cosine_sim is None or books is None:
        print("Error: Could not start the application due to missing files.")
    else:
        demo.launch(share=True)
    

    
    # How it Works
    gr.Markdown(
        """
        <div style="margin-top: 24px; padding: 20px; background: white; border-radius: 12px;">
            <h3 style="color: #000000; margin-bottom: 15px;">🤔 How It Works</h3>
            <ol>
                <li style="color: #000000;">Enter the title of a book you enjoyed</li>
                <li style="color: #000000;">Or copy example from the provided examples</li>
                <li style="color: #000000;">Choose how many recommendations you want (1-10)</li>
                <li style="color: #000000;">Click the "Get Recommendations" button</li>
                <li style="color: #000000;">Discover new books tailored to your taste!</li>
            </ol>
        </div>
        """
    )

    # Footer
    gr.Markdown(
        """
        <div style="text-align: center; margin-top: 30px;">
            <p style="color: #000000;">Made with ❤️ for book lovers | Version 2.1</p>
            <p style="color: #000000; font-size: 0.8em;">Powered by AI and curated with care</p>
        </div>
        """
    )

    # Set up click event
    recommend_button.click(
        book_recommender_interface,
        inputs=[book_name, num_recommendations],
        outputs=output
    )

if __name__ == "__main__":
    if tfidf is None or book_cosine_sim is None or books is None:
        print("Error: Could not start the application due to missing files.")
    else:
        demo.launch(share=True)