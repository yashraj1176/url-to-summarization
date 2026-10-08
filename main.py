import validators
import streamlit as st

from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import (
    UnstructuredURLLoader,
    YoutubeLoader
)


## Streamlit app
st.set_page_config(
    page_title="URL Summarization",
    page_icon="📝"
)

st.title("URL Summarization")
st.subheader("Summarize any URL or Youtube video in seconds using Groq LLM")
st.subheader("abhi kar ke deta hu")


## Get the Groq API key and URL from the user
with st.sidebar:

    groq_api_key = st.text_input(
        "Groq API key",
        value="",
        type="password"
    )


generic_url = st.text_input(
    "URL",
    label_visibility="collapsed"
)


## Prompt template
prompt_template = """
You are a helpful assistant that summarizes the content of a URL or Youtube video.

Content:
{text}

Please provide a clear and concise summary.
"""


prompt = PromptTemplate(
    template=prompt_template,
    input_variables=["text"]
)


## Summarize button
if st.button("Summarize the content from YT or website"):

    ## Check API key
    if not groq_api_key:

        st.error("Please enter your Groq API key in the sidebar.")

    ## Check URL
    elif not validators.url(generic_url):

        st.error("Please enter a valid URL.")

    else:

        try:

            with st.spinner("Summarizing the content..."):

                ## Groq LLM
                llm = ChatGroq(
                    api_key=groq_api_key,
                    model="openai/gpt-oss-20b",
                    temperature=0
                )


                ## YouTube URL
                if "youtube.com" in generic_url or "youtu.be" in generic_url:

                    loader = YoutubeLoader.from_youtube_url(
                        generic_url,
                        add_video_info=False
                    )


                ## Normal website URL
                else:

                    loader = UnstructuredURLLoader(
                        urls=[generic_url],
                        ssl_verify=False,
                        headers={
                            "User-Agent": (
                                "Mozilla/5.0 "
                                "(Windows NT 10.0; Win64; x64) "
                                "AppleWebKit/537.36 "
                                "(KHTML, like Gecko) "
                                "Chrome/58.0.3029.110 "
                                "Safari/537.3"
                            )
                        }
                    )


                ## Load the content
                data = loader.load()


                ## Check if content was found
                if not data:

                    st.error(
                        "Could not extract any content from this URL."
                    )

                    st.stop()


                ## Create summarization chain
                chain = load_summarize_chain(
                    llm,
                    chain_type="stuff",
                    prompt=prompt
                )


                ## Generate summary
                output_summary = chain.invoke(data)


                ## Display summary
                if isinstance(output_summary, dict):

                    st.success(
                        output_summary.get(
                            "output_text",
                            str(output_summary)
                        )
                    )

                else:

                    st.success(output_summary)


        except Exception as e:

            st.error("An error occurred while processing the URL.")

            st.exception(e)
