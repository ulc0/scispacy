```{mermaid}
graph LR
    subgraph CandidateGeneration
        LinkerPaths-->UmlsLinkerPaths
        LinkerPaths-->MeshLinkerpaths
        LinkerPaths-->GeneOntologyLinkerPaths
        LinkerPaths-->HumanPhenotypeOntology
        LinkerPaths-->RxNormLinkerPaths
    subgraph MentionCandidate
        LoadApproximateNearestNeighbor
    end
    nmslib_knn_with_zero_vectors
    create_tfidf_ann_index
    end


```