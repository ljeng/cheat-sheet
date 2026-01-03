# A Distributed Hash Table System

## Column Families in Databases

```mermaid
graph TD
    A[Google Bigtable] -->|inherited concept| B[HBase<br/>Apache Project]
    A -->|inherited concept| C[Cassandra<br/>Apache Project]
    A -.->|introduced| D[Column Families]
    B -.->|implements| D
    C -.->|implements| D
    D -->|organizes| E[Columns grouped together]
    D -->|provides| F[Storage & access patterns]
    style A fill:#4285f4,stroke:#333,stroke-width:2px,color:#fff
    style B fill:#ff6b35,stroke:#333,stroke-width:2px,color:#fff
    style C fill:#1287a8,stroke:#333,stroke-width:2px,color:#fff
    style D fill:#34a853,stroke:#333,stroke-width:2px,color:#fff
    style E fill:#fbbc04,stroke:#333,stroke-width:1px
    style F fill:#fbbc04,stroke:#333,stroke-width:1px

```


It's misleading to call Cassandra and HBase column-oriented. The Bigtable model is mostly row-oriented.

```mermaid
graph TB
    RowKey["Row Key<br/>All columns from a row stored together"]
    
    subgraph Table["Table<br/>Unbounded Columns"]
        direction TB
        TableTop[ ]
        subgraph CF1["Column Family 1<br/>Static, small number"]
            direction LR
            CK1["Column key: family:qualifier1"]
            CK2["Column key: family:qualifier2"]
            CK3["Column key: family:qualifierN"]
            CK1 --> Data1["Same type data compressed together"]
            CK2 --> Data1
            CK3 --> Data1
        end
        subgraph CF2["Column Family: 'language'"]
            direction TB
            LangKey["Column key: language:referring_site_name"]
            LangKey --> LangData["Cell content: link text"]
            Note1["Example: language:cnn.com -> 'Breaking News'"]
        end
        subgraph CF3["Column Family N"]
            CKN["Column keys: family:qualifier"]
        end
        CF1 --> CF2 --> CF3
        TableTop --> CF1
    end
    subgraph Controls["Column-family-level Controls"]
        direction TB
        AC["Access Control"]
        DM["Disk Management"]
        MA["Memory Accounting"]
    end
    subgraph Apps["Application Types"]
        direction TB
        App1["Read base data"]
        App2["Generate derived column families"]
    end
    RowKey --> Table
    Table -.-> Controls
    Table --> Apps
    style CF1 fill:#e1f5ff
    style CF2 fill:#fff4e1
    style CF3 fill:#e1ffe1
    style Controls fill:#ffe1e1
    style Apps fill:#f0e1ff
    style RowKey fill:#f5f5f5
    style TableTop fill:none,stroke:none

```

```mermaid
graph TB
    subgraph Webtable["Webtable<br/>BigTable"]
        subgraph Row1["Row: com.cnn.www"]
            CF1["Column family: language"]
            Col1["language:en"]
            Col2["language:es"]
            Col3["language:fr"]
            CF1 --> Col1
            CF1 --> Col2
            CF1 --> Col3
            Val1["Value: 'English'<br/>Timestamp: t1"]
            Val2["Value: 'Spanish'<br/>Timestamp: t2"]
            Val3["Value: 'French'<br/>Timestamp: t3"]
            Col1 -.-> Val1
            Col2 -.-> Val2
            Col3 -.-> Val3
        end
        subgraph Row2["Row: com.google.www"]
            CF2["Column family: language"]
            Col4["language:en"]
            CF2 --> Col4
            Val4["Value: 'English'<br/>Timestamp: t1"]
            Col4 -.-> Val4
        end
    end
    style CF1 fill:#e1f5ff
    style CF2 fill:#e1f5ff
    style Col1 fill:#fff4e1
    style Col2 fill:#fff4e1
    style Col3 fill:#fff4e1
    style Col4 fill:#fff4e1
    style Val1 fill:#f0f0f0
    style Val2 fill:#f0f0f0
    style Val3 fill:#f0f0f0
    style Val4 fill:#f0f0f0

```

Each column key in the **anchor family** represents a single anchor. These controls allow us to manage applications that add new base data and read-only applications with restricted visibility[^1].

[^1]: excluding certain families for privacy reasons
