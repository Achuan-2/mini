# pandoc模板

# 引用样式

引用1 [@kucera2020prostate] 引用2 [@sevastre2022intracellular]
中文引用3[@董文鸳2011我国谷歌学术搜索研究综述]
重复引用 [@kucera2020prostate] 
引用多个 [@kucera2020prostate; @sevastre2022intracellular]


# 标题样式

## 二级标题

### 三级标题

#### 四级标题

##### 五级标题

###### 六级标题

## 正文

行首缩进两个字段

## 代码块

在Word中代码段对应的样式是“Source Code”样式。

```bash
pandoc --citeproc --number-sections \
--csl china-national-standard-gb-t-7714-2015-author-date.csl \
--bibliography ref.bib -M reference-section-title="参考文献" \
-M link-citations=true --reference-doc ref.docx input.md -o main.docx
```

* ​`pandoc`​：执行 Pandoc 命令
* ​`--citeproc`​：处理文献引用，也可用 `-C`​ 代替
* ​`--number-sections`​：对各级标题编号，形如 `1, 1.1, 1.1.1`​，也可用 `-N`​ 代替
* ​`--csl china-national-standard-gb-t-7714-2015-author-date.csl`​：指定参考文献样式，这里使用的是 GB/T 7714-2015 的著者-出版年制格式，更多样式可以前往 [Zotero Style Repository](https://www.zotero.org/styles) 下载
* ​`--bibliography ref.bib`​：引文数据文件，即前文由 Better BibTeX for Zotero 导出的 `ref.bib`​
* ​`-M reference-section-title="参考文献"`​：设置参考文献表的标题为「参考文献」，不编号
* ​`-M link-citations=true`​：设置正文引用可以超链接到参考文献表中相应的条目，默认为 `false`​
* ​`--reference-doc ref.docx`​：参考的 DOCX 文件格式，根据 [Pandoc 使用手册](https://pandoc.org/MANUAL.html#option--reference-doc)，最好的方式是通过命令 `pandoc -o custom-reference.docx --print-default-data-file reference.docx`​ 得到 Pandoc 的默认 DOCX 文件，然后用 Microsoft Word 打开这个文件，根据你的喜好进行修改
* ​`input.md`​：存储文章内容的 Markdown 文件
* ​`-o main.docx`​：输出 DOCX 文件
* ​`\`​：反斜杠，表示换行，你也可以删除它，把所有命令写在一行。

## 表格

| header 1 | header 2 |
| :--------: | :--------: |
|  cell 1  |  cell 2  |
|  cell 3  |  cell 4  |
|  cell 5  |  cell 6  |


## 图片

![Snipaste_2022-11-04_00-35-02](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fstatic.seekingalpha.com%2Fuploads%2F2017%2F12%2F3%2F48200183-15122926541783805_origin.jpg&f=1&nofb=1&ipt=a3fc20c9244d2dceefe16cd84ee4b82b5a0b172d9f8e92f48ae847eadf1a78bd&ipo=images "baidu")​

## 列表

有序列表

1. 1
2. 2
3. 3

无序列表

* 1
* 2
* 3

## 引述块

> 这是一段引述块
>