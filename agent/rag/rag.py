from langchain_chroma import Chroma
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from pathlib import Path

from langchain_community.embeddings import DashScopeEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

from utils.key import dashscope_api_key


class Rag:
    def __init__(self):
        self.vector_store = Chroma(
            collection_name="rag",
            embedding_function=DashScopeEmbeddings(
                model="text-embedding-v4",
                dashscope_api_key= dashscope_api_key
            ),
            persist_directory = "./chroma_db"
        )

    def add_knowledge(self):
        # 目标文件夹绝对路径
        knowledge_dir = Path("../agent/knowledge").resolve()

        # 核心：用 loader_kwargs 传递编码
        loader = DirectoryLoader(
            path=str(knowledge_dir),
            glob="**/*.txt",  # 加载所有 txt 文件
            loader_cls=TextLoader,  # 使用 TextLoader
            loader_kwargs={  # 传递编码参数
                "encoding": "utf-8"
            },
            use_multithreading=True
        )

        docs = loader.load()
        # 文档切分
        text_splitter = RecursiveCharacterTextSplitter(
            separators=["\n", " ", ""],
            chunk_size=100,
            chunk_overlap=0
        )
        texts = text_splitter.split_text(docs[0].page_content)
        for i in texts:
            self.vector_store.add_texts([i])
        return


    def search_knowledge(self,query):
        similar_docs = self.vector_store.similarity_search(query, k=10)
        return similar_docs


