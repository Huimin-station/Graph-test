import datetime
from typing import List

from langchain_chroma import Chroma
from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings import DashScopeEmbeddings
from utils.key import dashscope_api_key
print(datetime.datetime.now())

# 文档加载器
loader = TextLoader(
    "新年知识.txt",
    encoding="utf-8"
)
documents = loader.load()
print("-"*20)
print("分词之前的数据")
print( documents)
print("-"*20)


from langchain_text_splitters import RecursiveCharacterTextSplitter


# 创建分词器
text_splitter = RecursiveCharacterTextSplitter(
    separators=["\n", " ", ""],
    chunk_size=100,
    chunk_overlap=0)
print("-"*20)
print("分词之后的数据")
texts = text_splitter.split_text(documents[0].page_content)
print(texts)
print("-"*20)
# for i in texts:
#     print("-"*20)
#     print(i)


model = "text-embedding-v4"
# 向量数据库
vector_store = Chroma(
            collection_name="rag",
            embedding_function=DashScopeEmbeddings(
                model="text-embedding-v4",
                dashscope_api_key= dashscope_api_key
            ),
            persist_directory="./chroma_db",
        )

# 写入向量数据库
for i in texts:
    vector_store.add_texts([i])
# 相似度搜索
similar_docs = vector_store.similarity_search("天河水", k=1)
print(similar_docs)