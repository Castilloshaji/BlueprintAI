from app.ai.generators.blueprint_generator import blueprint_generator


blueprint = blueprint_generator.generate(
    "Build an AI Hospital Management System"
)

print(blueprint)