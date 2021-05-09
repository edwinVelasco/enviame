const { Router } = require('express')
const { check } = require('express-validator')
const { existCompany, existsCompanyId } = require('../helpers/db-validators')
const { validCompany } = require('../middlewares/valid_company')

const {
    companyGet,
    companyPost,
    companyPut,
    companyPatch,
    companyDelete,
    companyFakerPost} = require('../controllers/company')

const router = Router();

router.get('/', companyGet)
router.post('/', [
    check('name', 'name is required').not().isEmpty(),
    check('nit', 'nit is required').not().isEmpty(),
    check('nit').custom(existCompany),
    validCompany,
], companyPost)
router.put('/:id', [
    check('id', 'Not is a MongoID valid').isMongoId(),
    check('name', 'name is required').not().isEmpty(),
    check('nit', 'nit is required').not().isEmpty(),
    check('id').custom(existsCompanyId),
    validCompany,
], companyPut)
router.delete('/:id',[
    check('id', 'Not is a MongoID valid').isMongoId(),
    check('id').custom(existsCompanyId),
    validCompany
    ],companyDelete)
router.patch('/:id', companyPatch)



router.post('/faker', [
    check('n', 'n is required').not().isEmpty(),
    validCompany,
], companyFakerPost)


module.exports = router;
