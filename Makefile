all: generate_graphene generate_Mg

generate_graphene:
	@echo "Making graphene cell..."
	@python3 GrapheneEditor.py

generate_Mg:
	@echo "Making Mg-12..."
	@python3 MgEditor.py
