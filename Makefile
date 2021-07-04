all: generate_graphene generate_Mn generate_combination

generate_graphene:
	@echo "Making graphene cell..."
	@python3 GrapheneEditor.py

generate_Mn:
	@echo "Making Mn-12..."
	@python3 MnEditor.py

generate_combination:
	@echo "Combining system..."
	@python3 CombineMn_Graphene.py