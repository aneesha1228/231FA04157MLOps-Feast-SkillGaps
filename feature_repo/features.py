from datetime import timedelta

from feast import Entity, FeatureView, Field
from feast.types import Float32, Int64
from feast.infra.offline_stores.file_source import FileSource


student = Entity(
    name="student_id",
    join_keys=["student_id"],
    description="Unique identifier for each final-year student"
)


skill_gap_source = FileSource(
    path="data/skill_gap_features.parquet",
    timestamp_field="event_timestamp"
)


skill_gap_features = FeatureView(
    name="student_skill_gap_features",
    entities=[student],
    ttl=timedelta(days=365),
    schema=[
        Field(name="Coding_Score", dtype=Float32),
        Field(name="Aptitude_Score", dtype=Float32),
        Field(name="Communication_Score", dtype=Float32),
        Field(name="Technical_Score", dtype=Float32),
        Field(name="Projects_Completed", dtype=Int64),
        Field(name="Certifications", dtype=Int64),
        Field(name="Internships", dtype=Int64),
        Field(name="Placement_Readiness_Score", dtype=Float32),
        Field(name="technical_average", dtype=Float32),
        Field(name="experience_score", dtype=Float32),
        Field(name="skill_strength_score", dtype=Float32),
    ],
    source=skill_gap_source,
)
